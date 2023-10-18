"""
example04.py - 单线程版本爬虫
"""
import os

import requests


def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/beauty/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    if not os.path.exists('images/beauty'):
        os.makedirs('images/beauty')
    for page in range(3):
        resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}')
        '''
        'list': [{'id': '1cda4038e60a15b5648ab44fa485eb1e', 'index': 1, 'grpmd5': '5c47f18aa8dd2884c289bf9ab4884e3f', 'grpseq': '1', 'grpcnt': '9', 'imgkey': 't01c54f48ecb0bfb4e8.jpg', 'width': '750', 'height': '1125', 'title': '夏季清纯自然美女衬衫短裙唯美小清新梦幻尤物jk制服写真', 'imgurl': 'https://img.gzhuibei.com/d/file/2020/07/02/0a0b25b4b3cacbd6c17163204aaabcc9.jpg', 'purl': 'http://www.48679.com/html/6348.html', 'site': 'www.48679.com', 'imgsize': '119', 'label': '萌女', 'sitename': '48679图库', 'siteid': '2722069277', 'src': '1', 'fnum': '0', 'qhimg_thumb_width': 133, 'qhimg_thumb_height': 200, 'qhimg_downurl': 'https://dl.image.so.com/d?imgurl=https%3A%2F%2Fp2.ssl.qhimgs1.com%2Ft01c54f48ecb0bfb4e8.jpg&purl=https%3A%2F%2Fimage.so.com%2F%3Fsrc%3Ddl.image&key=c243e844a1', 'qhimg_url': 'https://p2.ssl.qhimgs1.com/t01c54f48ecb0bfb4e8.jpg', 'qhimg_thumb': 'https://p2.ssl.qhimgs1.com/sdr/200_200_/t01c54f48ecb0bfb4e8.jpg', 'qhimg_qr_key': '18573a3181', 'tag': '119', 'rdate': '1595917805', 'ins_time': '2020-07-28 14:30:05', 'dsptime': '', 'summary': [], 'pic_desc': '夏季清纯自然美女衬衫短裙唯美小清新梦幻尤物jk制服写真'},
        '''
        print(resp.json())
        exit()
        if resp.status_code == 200:
            pic_dict_list = resp.json()['list']
            for pic_dict in pic_dict_list:
                download_picture(pic_dict['qhimg_url'])

if __name__ == '__main__':
    main()