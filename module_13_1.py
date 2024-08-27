import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Паша', 3))
    task2 = asyncio.create_task(start_strongman('Саша', 4))
    task3 = asyncio.create_task(start_strongman('Вася', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
