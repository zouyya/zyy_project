# coding:utf-8
import os
import logging
from AW.common.operate import Operate
from AW.common.config import *

class Logger(object):
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)  # 进行初始化
        self.logger.setLevel(logging.DEBUG)  # 日志等级为debug

    def getLog(self):
        tm = Operate().getTime()
        # 创建一个handler，用于写入日志文件
        try:
            os.makedirs(log_path)
        except:
            pass
        log_name = log_path + tm + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        return self.logger

    # 打印日志至窗口
    def printLog(self, content):
        self.logger.info(content)