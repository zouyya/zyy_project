from AW.action.action_wms import action_wms
from AW.function.wms import wms
from AW.common.logger import Logger
import time

class Wms(object):
    def __init__(self, driver):
        self.wms = wms(driver)
        self.action_wms = action_wms(self.wms)

    # 登陆WMS后选择业务
    # @param username:用户名
    # @param password:密码
    # @param business:业务名称
    def login_and_choose_business(self, username, password, business):
        Logger(logger='TestLog').printLog(u"登陆WMS后选择%s业务" % business)
        self.wms.Login(username, password)
        time.sleep(2)
        self.wms.Click_Login_Button()
        time.sleep(4)
        self.wms.Click_Orchestration_Button(business)
