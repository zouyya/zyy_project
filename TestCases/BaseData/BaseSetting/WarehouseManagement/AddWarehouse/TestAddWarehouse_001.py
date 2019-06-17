# coding:utf-8
import unittest
from selenium import webdriver
from AW.common.screenShot import *
from AW.service.Wms import Wms
from AW.service.BaseData import BaseData

class TestAddWarehouse_001(unittest.TestCase):
    def setUp(self):
        # 选择浏览器
        self.driver = webdriver.Chrome()
        # 要打开的链接地址
        self.driver.get('http://172.31.75.173:8080/login.html')
        # 放大窗口
        self.driver.maximize_window()

    def testAddWarehouse(self):
        # 实例化对象
        comWms = Wms(self.driver)
        comBaseData = BaseData(self.driver)
        time.sleep(2)
        # 登陆WMS后选择基础资料
        comWms.login_and_choose_business("zouyy", "123", u"基础资料")
        time.sleep(2)
        # 进入商品资料-仓库管理-新增仓库
        comBaseData.add_warehouse()
        time.sleep(2)
        # 校验进入新增仓库界面成功
        ele = comWms.action_wms.findElementsByWay("layui-form-label", "class_name")
        self.assertEqual(len(ele), 11, u"没有进入新增仓库界面")

    def tearDown(self):
        self.driver.quit()
