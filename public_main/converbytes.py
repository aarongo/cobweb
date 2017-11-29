#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

import math


def convertBytes(bytes, lst=['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']):
    i = int(math.floor( # 舍弃小数点，取小
             math.log(bytes, 1024) # 求对数(对数：若 a**b = N 则 b 叫做以 a 为底 N 的对数)
            ))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + " " + lst[i]) % (bytes/math.pow(1024, i))


def main(bytes):
    lst = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    #bytes = input('Bytes: ')
    return convertBytes(bytes, lst)


# if __name__ == '__main__':
#     main(bytes=1970368389120)