#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 上午11:54
# @Author  : Jun
# @File    : test.py

import sys
print('my os is :', sys.platform)
if sys.platform == 'linux':
    print('remote is working')
else:
    print('local is working')