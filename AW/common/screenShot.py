from AW.common.config import *
from functools import wraps

class screenShot(object):
    def __init__(self, driver):
        self.driver = driver

    # 截图
    def ScreenShot(self):
        tm = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())  # 格式化时间
        screenShot_path = os.path.dirname(os.path.abspath('..')) + '/Report/' + tm + "/screenShot/"
        if screenShot_path in os.getcwd():
            pass
        else:
            os.makedirs(screenShot_path)
        filename = screenShot_path + tm + '.png'
        self.driver.get_screenshot_as_file(filename)

#装饰器
def get_image_except(function):
    @wraps(function)
    def errorImage(self):
        try:
            function(self)
        except:
            try:
                os.makedirs(screenShotPath)
            except:
                pass
            print('脚本发生错误')
        else:
            print(' %s 脚本运行正常' %
                (function.__name__)
                )

    return errorImage