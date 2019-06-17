# coding:utf-8
import os
import logging
import time


class Operate(object):

    # 获取当前时间
    def getTime(self):
        tm = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())  # 格式化时间
        return tm

    # 获取当前文件