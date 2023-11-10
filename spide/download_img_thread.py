import os
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(
        url=url,
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
        # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
        # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
        headers={'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    )
    if resp.status_code == 200:
        with open(f'images/beauty1/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    start_time = time.time()
    if not os.path.exists('images/beauty1'):
        os.makedirs('images/beauty1')
    with ThreadPoolExecutor(max_workers=16) as pool:
        for page in range(1):
            resp = requests.get(
            url=f'https://image.so.com/zjl?ch=beauty&sn={page * 30}',
            # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
            # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
            # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
            headers={'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    )
            if resp.status_code == 200:
                pic_dict_list = resp.json()['list']
                for pic_dict in pic_dict_list:
                    pool.submit(download_picture, pic_dict['qhimg_url'])
    print(f'下载使用时间：{(time.time() - start_time):.3f} S')


if __name__ == '__main__':
    main()