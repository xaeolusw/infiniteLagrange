import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    print (mydict['cars'][0]['brand'])
    exit()
    try:
        """
        json中重要的几个函数：
        `dump` - 将Python对象按照JSON格式序列化到文件中
        `dumps` - 将Python对象处理成JSON格式的字符串
        `load` - 将文件中的JSON数据反序列化成对象
        `loads` - 将字符串的内容反序列化成Python对象
        """
        with open('test/data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()