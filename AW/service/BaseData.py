from AW.action.action_basedata import action_basedata
from AW.function.basedata import basedata
from AW.function.wms import wms
from AW.common.logger import Logger

class BaseData(object):
    def __init__(self, driver):
        self.basedata = basedata(driver)
        self.wms = wms(driver)
        self.action_basedata = action_basedata(self.basedata)

    # 仓库管理-新增仓库
    def add_warehouse(self):
        Logger(logger='TestLog').printLog(u"新增仓库")
        self.basedata.Click_Process_Button(u"基础设置")
        self.basedata.Click_BaseSetting_Button(u"仓库管理")
        self.wms.Switch_To_Frame('//*[@id="container"]/div/div[2]/div[2]/iframe')
        self.wms.Click_Function_Button(u"新增")
        self.wms.Back_To_Frame()
        self.wms.Switch_To_Frame('//*[@id="container"]/div/div[2]/div[3]/iframe')
