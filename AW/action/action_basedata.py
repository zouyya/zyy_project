from AW.common.logger import Logger

class action_basedata():
    ##初始化
    # @param funbasedata basedata function对象
    def __init__(self, funbasedata):
        self.basedata = funbasedata

    ## 登陆网站
    # @param username:用户名
    # @param password:密码
    def login(self, username, password):
        Logger(logger='TestLog').printLog(u"登陆网站")
        self.wms.Login(username, password)
