from AW.common.logger import Logger

class action_wms():
    ##初始化
    # @param funwms wms function对象
    def __init__(self, funwms):
        self.wms = funwms

    ## 登陆网站
    # @param username:用户名
    # @param password:密码
    def login(self, username, password):
        Logger(logger='TestLog').printLog(u"登陆网站")
        self.wms.Login(username, password)

    ## 点击登陆按钮
    def click_login_button(self):
        Logger(logger='TestLog').printLog(u"点击登陆按钮")
        self.wms.Click_Login_Button()

    ## 通过各种方式定位某元素
    def findElementByWay(self, element, way):
        Logger(logger='TestLog').printLog(u"通过%s方式查找元素%s" % (way, element))
        return self.wms.FindElementByWay(element, way)

    ## 通过各种方式定位某元素
    def findElementsByWay(self, element, way):
        Logger(logger='TestLog').printLog(u"通过%s方式查找元素%s" % (way, element))
        return self.wms.FindElementsByWay(element, way)

    ## 点击新增/修改/作废功能按钮
    # @param button:按钮名称
    def click_function_button(self, button):
        Logger(logger='TestLog').printLog(u"点击%s功能按钮" % button)
        self.wms.Click_Function_Button()

    ## 点击业务流程
    # @param button:业务流程名称 如基础资料，进货管理，出货管理，库内管理，报表管理，系统管理等
    def click_orchestration_button(self, button):
        Logger(logger='TestLog').printLog(u"点击%s业务流程" % button)
        self.wms.Click_Orchestration_Button()

    ## 切换iframe，使界面定位到元素
    # @param element:iframe的定位
    def switch_to_frame(self, element):
        Logger(logger='TestLog').printLog(u"切换iframe，使界面定位到元素")
        self.wms.Switch_To_Frame(element)
