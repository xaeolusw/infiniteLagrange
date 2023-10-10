import time

from concurrent.futures import ThreadPoolExecutor
import threading


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.RLock()

    def deposit(self, money):
        # 通过上下文语法获得锁和释放锁
        if money < 0:
            print(f'取钱 {money}')
            while True:
                threading.Condition.wait_for(self.balance > 0)
                time.sleep(0.02)
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
            print(self.balance)


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(5):
            pool.submit(account.deposit, -1)
            pool.submit(account.deposit, 1)
    print(account.balance)


if __name__ == '__main__':
    main()