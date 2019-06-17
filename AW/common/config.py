# coding:utf-8
import os
import logging
import time
from AW.common.operate import Operate

tm = Operate().getTime()

# 获取当前路径
currPath = os.path.split(os.path.realpath(__file__))[0]

# 保存日志路径
log_path = os.path.dirname(os.path.abspath('..')) + '/Report/' + tm + "/logs/"

# 保存截图位置
screenShotPath = os.path.join(log_path, "..") + "/screenShot/"