#encoding=utf-8
from utils.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from interface.create_script import create_script
import time,sys
sys.path.append("./script")
reload(sys)
sys.setdefaultencoding("utf8")


if __name__ == "__main__":
    #生成测试脚本
    create_script()
    #执行测试脚本
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    test_dir="./script"
    # 当前工程目录的script目录下，找下划线test.py结尾的文件，把他们加载成测试用例集合，赋给变量testsuit
    testsuit = defaultTestLoader.discover(test_dir,pattern ="*_test.py")
    #测试报告文件名：report目录下，时间命名的，以result.html结尾
    filename = "./report/" + now + "result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="接口自动化测试",description="接口自动化测试结果报告")
    runner.run(testsuit)
    fp.close()