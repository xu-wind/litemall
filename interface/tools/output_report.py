from interface.tools.HTMLTestRunner import HTMLTestRunner
# 导包
import unittest

# 定义 测试套件
suite = unittest.defaultTestLoader.discover("../scripts", pattern="test_goods_report.py")

# 插件执行
with open('../report/report.html', "wb") as f:
    HTMLTestRunner(stream=f, title='添加商品接口自动化测试报告', description='win10 Chrome').run(suite)
