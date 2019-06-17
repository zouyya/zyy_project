#coding:utf-8
import unittest
import os
import time
from selenium import webdriver
from AW.HTML import HTMLTestRunnerCN

def testFull():
    testcase = unittest.TestSuite()
    case_dir = os.path.join(os.getcwd(), "TestCases\\Test_Web")
    # discover方法筛选出来的用例，循环添加到测试套件中
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='Test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            print(test_case, "test")
            testcase.addTest(test_case)
    return testcase

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filePath = 'F:\\NewProject\\src\\Report\\' + now + '_report.html'
    # 确定生成报告的路径
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title=u'自动化测试报告',
        # description='详细测试用例结果',    #不传默认为空
        tester=u"Findyou"
        # 测试人员名字，不传默认为QA
        )
    # 运行测试用例
    runner.run(testFull())
    fp.close()