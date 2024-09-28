import asyncio
import logging
import sys

import aiogram
from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.chat_action import ChatActionSender
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class UserState(StatesGroup):
    pol = State()
    age = State()
    growth = State()
    weight = State()


TOKEN = "7240600592:AAFXO1eHt9-vm58Y9DGdMEwJGykDE7HMpNY"

dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация'),
         KeyboardButton(text='Рассчитать')]
    ], resize_keyboard=True
)


kb = InlineKeyboardBuilder()

kb.add(InlineKeyboardButton(
    text="Рассчитать норму калорий",
    callback_data="calories"))
kb.add(InlineKeyboardButton(
    text="Формулы расчета",
    callback_data="formulas"))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! Я бот помогающий твоему здоровью.", reply_markup=menu)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message, state: FSMContext):
    print('Menu')
    await message.answer(
        "Выберите опцию:",
        reply_markup=kb.as_markup()
    )


@dp.callback_query(F.data == "formulas")
async def send_random_value(callback):
    await callback.message.answer("1. Упрощенный вариант формулы Миффлина-Сан Жеора:"
                                  "для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;"
                                  "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")


@dp.callback_query(F.data == "calories")
async def send_random_value(callback, state):
    await callback.message.answer('Введите свой пол m или f:')
    await state.set_state(UserState.pol)
    print("pol")


@dp.message(F.text, UserState.pol)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(pol=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(F.text, UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(F.text, UserState.growth)
async def set_aweight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес::')
    await state.set_state(UserState.weight)


@dp.message(F.text, UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 0
    if data['pol'] == "m":
        calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - (5 * int(data['age'])) + 5
        await message.answer("Ваша норма калорий в сутки : " + str(calories))
        await state.clear()
    else:
        calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - (5 * int(data['age'])) - 161
        await message.answer("Ваша норма калорий в сутки : " + str(calories))
        await state.clear()


@dp.message()
async def message_handler(message: Message) -> None:
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())