from appium import webdriver

from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options

from common import utils

from multiprocessing import Pool


class IOSDriver:
    """
    iOS驱动器
    """

    def get_driver(self):
        """
        :description: 使用Python-client请求Appium server创建session，并返回iOS driver
        :return: driver
        """
        options = XCUITestOptions()

        options.automation_name = "XCUITest"
        options.platform_name = "iOS"
        options.platform_version = "15.6"
        options.device_name = "Geekmister"
        options.udid = "f47eaa5706c3df37ca2d56eb63d0dd71328849d1"
        options.no_reset = True
        options.bundle_id = "com.tencent.ww"

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

        return driver

class AndroidDriver:
    """
    Android驱动器
    """

    def get_driver(self):
        options = UiAutomator2Options()

        options.automation_name = "Appium"
        options.platform_name = "Android"
        options.platform_version = "8.1"
        options.device_name = "device"
        options.no_reset = True
        options.app_package = "com.android.calculator2"
        options.app_activity = ".Calculator"
        options.udid = 'b96ba9fe'

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        ### ceshi

        return driver

def excetue(type, is_excetue):
    if(type == 1):
        ios_driver = IOSDriver()
        ios_driver.get_driver()
    else:
        android_driver = AndroidDriver()
        android_driver.get_driver()

if __name__ == '__main__':
    # android_driver = AndroidDriver()
    # android_driver.get_driver()
    pool = Pool(1)
    types = [[1, True], [2, True]]
    for type in types:
        pool.apply(excetue, (type[0], type[1]))