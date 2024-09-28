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


class UserState(StatesGroup):
    pol = State()
    age = State()
    growth = State()
    weight = State()


TOKEN = "7240600592:AAFXO1eHt9-vm58Y9DGdMEwJGykDE7HMpNY"

dp = Dispatcher()
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация'),
         KeyboardButton(text='Рассчитать')]
    ], resize_keyboard=True
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! Я бот помогающий твоему здоровью.", reply_markup=main_menu)


@dp.message(F.text == 'Рассчитать')
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой пол m или f:')
    await state.set_state(UserState.pol)


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