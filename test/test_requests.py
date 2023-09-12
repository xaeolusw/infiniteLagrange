from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('test/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    DownloadHanlder('http://www.nongli.net/img/20161208150954628.jpg').start()


if __name__ == '__main__':
    main()