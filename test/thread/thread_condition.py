from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account:
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.RLock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
                print(f'没钱了，帐号只有{self.balance}, 不够取出 {money}。')
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(f'{threading.current_thread().name} : {money} ====> {account.balance}')
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(f'{threading.current_thread().name} : {money} <==== {account.balance}')
        sleep(1)


def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(10):
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()