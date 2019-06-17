from AW.common.logger import Logger
from AW.function.wms import wms
import time

process = {0: u"基础设置", 1: u"商品资料", 2: u"条码设置", 3: u"SN码箱码", 4: u"列印集成"}
baseSetting = {0: u"仓库管理", 1: u"货主管理", 2: u"供应商管理", 3: u"SN码箱码", 4: u"列印集成"}

class basedata():
    def __init__(self, driver):
        self.driver = driver
        self.wms = wms(self.driver)
    ## 基础资料下，点击相关操作
    # @param button:操作名称
    def Click_Process_Button(self, button):
        Logger(logger='TestLog').printLog(u"基础资料下，点击%s" % button)
        # ele = self.driver.find_elements_by_tag_name("layui-nav-item")
        ele = self.driver.find_elements_by_xpath('//*[@id="10001_left"]/li')
        # 遍历出process字典里的所有内容
        for key, value in process.items():
            if button == value:
                ele[key].click()
        time.sleep(2)

    ## 基础设置下，点击相关操作
    # @param button:操作名称 例如仓库管理，货主管理，供应商管理等
    def Click_BaseSetting_Button(self, button):
        Logger(logger='TestLog').printLog(u"基础设置下，点击%s" % button)
        ele = self.driver.find_elements_by_xpath('//*[@id="10001_left"]/li[1]/dl/dd')
        # 遍历出baseSetting字典里的所有内容
        for key, value in baseSetting.items():
            if button == value:
                ele[key].click()
