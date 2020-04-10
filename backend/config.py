#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2020/1/1 13:14
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    通过设置window或者linux系统的环境变量，来区分dev,test,pro环境

    Usage Example
    -------------
    ::windows添加环境变量有两种方式：
    第一种方式 ：windows下，在“系统设置”——“环境变量”——“用户变量”下，点击“新建” 添加进
    第二种方式 ：pycharm-设置环境变量，点击pycharm右上角的“Edit Configuration”,
                然后点击environment variables末端的一个文件夹图标，进入第二个对话框，点击加号新增

    Flask生成SECRET_KEY
    >> import os
    >> os.urandom(24)
"""
import os

env_dist = os.environ


class Config:
    _SEEYOU_PLATFORM_ENV = env_dist.get('SEEYOU_PLATFORM_ENV', 'dev')  # （必填）
    _SEEYOU_PLATFORM_MONGO_HOST = env_dist.get('SEEYOU_PLATFORM_MONGO_HOST', '127.0.0.1')  # 数据库的地址和端口（必填）
    _SEEYOU_PLATFORM_MONGO_PORT = env_dist.get('SEEYOU_PLATFORM_MONGO_PORT', '27017')
    _SEEYOU_PLATFORM_MONGO_USERNAME = env_dist.get('SEEYOU_PLATFORM_MONGO_USERNAME')  # 表示数据库的帐号密码（若无可不填）
    _SEEYOU_PLATFORM_MONGO_PASSWORD = env_dist.get('SEEYOU_PLATFORM_MONGO_PASSWORD')
    _SEEYOU_PLATFORM_MONGO_DEFAULT_DBNAME = env_dist.get('SEEYOU_PLATFORM_MONGO_DEFAULT_DBNAME', 'test_mongodb')
    _SEEYOU_PLATFORM_NLP_SERVER_HOST = env_dist.get('SEEYOU_PLATFORM_NLP_SERVER_HOST', 'localhost')
    _SEEYOU_PLATFORM_SECRET_KEY = env_dist.get(
        'SEEYOU_PLATFORM_SECRET_KEY',
        b'2H\xf0\xd3|\xee{c\x9c}\xf4\x147E\xdf\xca\xaa\x17\xfd\x17\xd5[cD')

    def get_env(self):
        """获取环境变量"""
        return self._SEEYOU_PLATFORM_ENV

    def set_env(self, env):
        """设置环境变量"""
        self._SEEYOU_PLATFORM_ENV = env

    def get_nlp_server_host(self):
        """获取nlp bert as serving host"""
        return self._SEEYOU_PLATFORM_NLP_SERVER_HOST

    def set_nlp_server_host(self, host):
        """设置nlp bert as serving host"""
        self._SEEYOU_PLATFORM_NLP_SERVER_HOST = host

    def get_mongo_host(self):
        """获取mongo host"""
        return self._SEEYOU_PLATFORM_MONGO_HOST

    def set_mongo_host(self, host):
        """设置mongo host"""
        self._SEEYOU_PLATFORM_MONGO_HOST = host

    def get_mongo_port(self):
        """获取mongo port"""
        return self._SEEYOU_PLATFORM_MONGO_PORT

    def set_mongo_port(self, port):
        """设置mongo port"""
        self._SEEYOU_PLATFORM_MONGO_PORT = port

    def get_mongo_username(self):
        """获取mongo username"""
        return self._SEEYOU_PLATFORM_MONGO_USERNAME

    def set_mongo_username(self, username):
        """设置mongo username"""
        self._SEEYOU_PLATFORM_MONGO_USERNAME = username

    def get_mongo_password(self):
        """获取mongo password"""
        return self._SEEYOU_PLATFORM_MONGO_PASSWORD

    def set_mongo_password(self, password):
        """设置mongo password"""
        self._SEEYOU_PLATFORM_MONGO_PASSWORD = password

    def get_mongo_default_db_name(self):
        """获取mongo 默认链接DB名称"""
        return self._SEEYOU_PLATFORM_MONGO_DEFAULT_DBNAME

    def set_mongo_default_db_name(self, db_name):
        """设置mongo 默认链接DB名称"""
        self._SEEYOU_PLATFORM_MONGO_DEFAULT_DBNAME = db_name

    def get_secret_key(self):
        """获取密钥"""
        return self._SEEYOU_PLATFORM_SECRET_KEY

    def set_secret_key(self, secret_key):
        """设置密钥"""
        self._SEEYOU_PLATFORM_SECRET_KEY = secret_key


if __name__ == '__main__':
    config = Config()
    print('SEEYOU_PLATFORM_ENV: ----------> %s' % config.get_env())
    print('SEEYOU_PLATFORM_MONGO_HOST: ----------> %s' % config.get_mongo_host())
    print('SEEYOU_PLATFORM_MONGO_PORT: ----------> %s' % config.get_mongo_port())
    print('SEEYOU_PLATFORM_NLP_SERVER_HOST: ----------> %s' % config.get_nlp_server_host())
    print('SEEYOU_PLATFORM_MONGO_USERNAME: ----------> %s' % config.get_mongo_username())
    print('SEEYOU_PLATFORM_MONGO_PASSWORD: ----------> %s' % config.get_mongo_password())
    print('SEEYOU_PLATFORM_MONGO_DEFAULT_DBNAME: ----------> %s' % config.get_mongo_default_db_name())
    print('SEEYOU_PLATFORM_SECRET_KEY: ----------> %s' % config.get_secret_key())
