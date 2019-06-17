from AW.common.logger import Logger
import time

button_permission = {u"新增": "is_add", u"修改": "is_modify", u"作废": "is_delete", u"提交": "is_add",
                     u"审核": "is_add", u"结案": "is_add", u"导入": "is_import", u"导出": "is_export"}

class wms():
    def __init__(self, driver):
        self.driver = driver

    ## 登陆网站
    # @param username:用户名
    # @param password:密码
    def Login(self, username, password):
        Logger(logger='TestLog').printLog(u"用户名输入%s" % username)
        self.FindElementByWay("username", "id").send_keys(username)
        Logger(logger='TestLog').printLog(u"密码输入%s" % password)
        self.FindElementByWay("passwd", "id").send_keys(password)

    ## 点击登陆按钮
    def Click_Login_Button(self):
        Logger(logger='TestLog').printLog(u"点击登陆按钮")
        self.FindElementByWay("btn-submit", "id").click()

    ## 通过各种方式获取某元素(元素唯一）
    def FindElementByWay(self, element, way):
        Logger(logger='TestLog').printLog(u"通过%s方式查找元素%s" % (way, element))
        if way == "id":
            return self.driver.find_element_by_id(element)
        elif way == "class_name":
            return self.driver.find_element_by_class_name(element)
        elif way == "name":
            return self.driver.find_element_by_name(element)
        elif way == "tag name":
            return self.driver.find_element_by_tag_name(element)

    ## 通过各种方式获取某元素(元素不唯一）
    def FindElementsByWay(self, element, way):
        Logger(logger='TestLog').printLog(u"通过%s方式查找元素%s" % (way, element))
        if way == "class_name":
            return self.driver.find_elements_by_class_name(element)
        elif way == "tag_name":
            return self.driver.find_elements_by_tag_name(element)

    ## 点击新增/修改/作废等功能按钮
    # @param button:按钮名称 例如新增/修改/作废
    def Click_Function_Button(self, button):
        Logger(logger='TestLog').printLog(u"点击%s功能按钮" % button)
        # 遍历出button_permission字典里的所有内容
        for key, value in button_permission.items():
            if button == key:
                ele = self.FindElementByWay(value, "id")
                ele.click()


    ## 点击业务流程
    # @param business:业务流程名称 如基础资料，进货管理，出货管理，库内管理，报表管理，系统管理等
    def Click_Orchestration_Button(self, business):
        Logger(logger='TestLog').printLog(u"点击%s业务流程" % business)
        orchestration_list = [[u"基础资料", "10001"], [u"进货管理", "10002"], [u"出货管理", "10003"], [u"库内管理", "10004"],
                              [u"报表管理", "10005"], [u"系统管理", "10006"]]
        for i in range(6):
            if business in orchestration_list[i][0]:
                self.FindElementByWay(orchestration_list[i][1], "id").click()

    ## 切换iframe，使界面定位到元素
    # @param element:iframe的定位
    def Switch_To_Frame(self, element):
        Logger(logger='TestLog').printLog(u"切换到相应的iframe")
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(element))
        time.sleep(2)

    ## 切换默认的iframe
    def Back_To_Frame(self):
        Logger(logger='TestLog').printLog(u"切换默认的iframe")
        self.driver.switch_to.default_content()
        time.sleep(2)