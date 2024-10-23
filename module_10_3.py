from threading import Thread, Lock
import random
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        print(f'На депозите {self.balance} средств') # проверка количества средств

        for i in range(100):
            dep = random.randint(50, 500) # случайное число (сумма пополнения)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f'Пополнен: {dep}. Баланс: {self.balance}')
            # else:
            #     print(f'депозит закрыт на снятие, Баланс меньше 500')
    sleep(0.001)

    def take(self):

        for i in range(100):
            tk = random.randint(50, 500)
            print(f'Запрос на {tk}')

            if tk <= self.balance:
                self.balance = self.balance - tk
                print(f'Снятие: {tk}. Баланс: {self.balance}')

            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
