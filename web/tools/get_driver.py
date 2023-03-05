from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    __driver = None
    __app_driver = None

    @classmethod
    def get_web_driver(cls, url):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(5)  # 添加隐式等待可以避免操作过快导致报错问题
            cls.__driver.get(url)
        return cls.__driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None
        return cls.__driver

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 连接appium服务器,获取driver
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None
        return cls.__app_driver
