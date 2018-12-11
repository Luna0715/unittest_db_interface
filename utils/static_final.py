#encoding=utf-8
import os

#工程根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#数据库配置文件绝对路径
config_path = BASE_DIR + "/config/db_config.ini"

#测试脚本文件存放目录
SCRIPT_PATH = BASE_DIR + "/script"

code_head = '''#encoding=utf-8
import unittest, requests
from interface.pubilc_info import *
import os, sys,json
'''
# 无数据库链接时
class_head = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.base_url = "%s"
'''

# 有数据库链接时
class_head_db = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.dbd = DB_Data()
        self.base_url = "%s"
'''


class_end_db = '''
    def tearDown(self):
        self.dbd.close_connect()
'''
code_end = '''
if __name__ == '__main__':
    unittest.main()
'''

post_code = '''
    #测试方法名：test固定，拼接上filename+索引号,百分号s用filename和索引号替换
    def test_%s(self):
    #百分号s测试用例索引号
        """%s"""
        #需要实现依赖数据的处理，传参的参数值需要赋给payload
        %s
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        #响应code200是必须检测的，所以直接写出来，没有读数据库
        self.assertEqual(r.status_code, 200)
        #需要实现检测点的检测、数据存储
        %s
'''

get_code = '''\n
    def test_%s(self):
        """%s"""
        %s
        #get与post的区别在self.base_url + str(payload)
        r = requests.get(self.base_url + str(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''

check_code = '''
        check_point = %s
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))
'''


