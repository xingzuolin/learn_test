#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 上午11:27
# @Author  : Jun
# @File    : test1.py


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


if __name__ == '__main__':
    a = add(5, 6)
    b = mul(5, 6)
    c = a + b
    print(c)