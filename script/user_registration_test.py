#encoding=utf-8
import unittest, requests
from interface.pubilc_info import *
import os, sys,json

class User_Registration(unittest.TestCase):
    """用户注册"""
    def setUp(self):
        self.dbd = DB_Data()
        self.base_url = "http://39.106.41.11:8080/register/"

    #测试方法名：test固定，拼接上filename+索引号,百分号s用filename和索引号替换
    def test_user_registration_1(self):
    #百分号s测试用例索引号
        """1"""
        #需要实现依赖数据的处理，传参的参数值需要赋给payload
        payload = {"username":"lbbhehe","password":"wcx123wac1","email":"wcx@qq.com"}
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        #响应code200是必须检测的，所以直接写出来，没有读数据库
        self.assertEqual(r.status_code, 200)
        #需要实现检测点的检测、数据存储
        self.dbd.store_data(1,1,{"request":["username","password"],"response":["code"]},{"username":"lbbhehe","password":"wcx123wac1","email":"wcx@qq.com"},result)
        check_point = {"code":"00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def tearDown(self):
        self.dbd.close_connect()

if __name__ == '__main__':
    unittest.main()
