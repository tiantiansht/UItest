# coding:utf-8
import os
import HTMLTestRunner
import unittest

curPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
strtdir = os.path.join(curPath,"case")
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(strtdir,rule)
with open(curPath+"/report/result.html","wb") as f:
#runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(f,title="接口测试报告",description="报告如下")
    runner.run(discover)
