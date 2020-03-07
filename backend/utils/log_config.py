#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/4/2 14:46
# @Software: PyCharm
# @Author  : https://github.com/Valuebai/
"""
    封装python logging日志，命名为log_config.py
    ~~~~~~~~~~~~~~~

    - 修改日志保存路径，否则使用默认上一层目录的./logs/
    - 使用：from common.log_config import logger     # common表示本文件放在的文件夹
        logger.info('打印info日志')
        logger.error('打印error日志')


    注意：
    - flask 有自带的log，使用本文件后会覆盖flask自带的

    - 无法自动删除日志 & 日志没有分隔记录
      使用TimedRotatingFileHandler创建时间循环日志，suffix需写成对应格式，如下
      参数中的when="D", or MIDNIGHT 天，file_handler.suffix = "%Y-%m-%d.log"
      参数中的when="S" 秒，file_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"

    - 多进程写入同一日志文件冲突问题
      >> PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。

      >> 类似：2.使用多进程初始化同一日志模块，会导致日志备份报错，因为两个进程同时打开了日志文件，在重命名时会出现
                 WindowsError: [Error 32]错误，该错误是由于文件已被打开，
        按照官方文档的介绍，logging 是线程安全的，也就是说，在一个进程内的多个线程同时往同一个文件写日志是安全的。但是（对，
        这里有个但是）多个进程往同一个文件写日志不是安全的,为了解决这个问题，可使用 ConcurrentLogHandler，
        ConcurrentLogHandler 可以在多进程环境下安全的将日志写入到同一个文件，并且可以在日志文件达到特定大小时，分割日志文件。
      >> 在默认的 logging 模块中，有个 TimedRotatingFileHandler 类，可以按时间分割日志文件，
        可惜 ConcurrentLogHandler 不支持这种按时间分割日志文件的方式。(用单例模式无法解决!)

      >> 解决方法：1、继承TimedRotatingFileHandler重载，修改里面的东西
      >> 解决方法：2、直接使用开源的代码来用，本文使用的是concurrent_log  ！！！
                     安装：pip install concurrent_log
                     url: https://github.com/huanghyw/concurrent_log
                     使用from concurrent_log import ConcurrentTimedRotatingFileHandler
                     直接在用TimedRotatingFileHandler替换为ConcurrentTimedRotatingFileHandler即可，其他代码不需要任何改动
                     ！！！后面在使用过程中有问题再看看！！！

      >> 解决方法：3、建议使用sentry 来记录日志
"""

import os
import logging.config
from concurrent_log import ConcurrentTimedRotatingFileHandler  # 解决logging多线程问题


class GetLogger:
    """
    自定义logging，方便使用
    """

    def __init__(self, logs_dir=None, logs_level=logging.INFO):
        self.logs_dir = logs_dir  # 日志路径
        self.log_name = r'log.log'  # 日志名称
        self.logs_level = logs_level  # 日志级别
        # 日志的输出格式
        self.log_formatter = logging.Formatter(
            '%(asctime)s [%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s')

        if logs_dir is None:
            sep = os.sep  # 自动匹配win,mac,linux 下的路径分隔符
            self.logs_dir = os.path.abspath(
                os.path.join(__file__, f"..{sep}..{sep}logs{sep}"))  # 设置日志保存路径

        # 如果logs文件夹不存在，则创建
        if os.path.exists(self.logs_dir) is False:
            os.mkdir(self.logs_dir)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        # 实例化root日志对象
        log_logger = logging.getLogger('root')

        # 设置日志的输出级别
        log_logger.setLevel(self.logs_level)
        if log_logger.handlers == []:  # 避免重复日志
            # 创建一个handler，用于输出到cmd窗口控制台
            console_handler = logging.StreamHandler()

            console_handler.setLevel(logging.INFO)  # 设置日志级别
            console_handler.setFormatter(self.log_formatter)  # 设置日志格式
            log_logger.addHandler(console_handler)

            # 建立一个循环文件handler来把日志记录在文件里
            file_handler = ConcurrentTimedRotatingFileHandler(
                filename=self.logs_dir + os.sep + self.log_name,  # 定义日志的存储
                when="MIDNIGHT",  # 按照日期进行切分when = D： 表示按天进行切分,or self.when == 'MIDNIGHT'
                interval=1,  # interval = 1： 每天都切分。 比如interval = 2就表示两天切分一下。
                backupCount=30,  # 最多存放日志的数量
                encoding="UTF-8",  # 使用UTF - 8的编码来写日志
                delay=False,
                # utc = True: 使用UTC + 0的时间来记录 （一般docker镜像默认也是UTC + 0）
            )
            file_handler.doRollover()
            file_handler.suffix = "%Y-%m-%d.log"
            file_handler.setLevel(logging.DEBUG)  # 设置日志级别
            file_handler.setFormatter(self.log_formatter)  # 设置日志格式
            log_logger.addHandler(file_handler)

        return log_logger


logger = GetLogger().get_logger()

if __name__ == "__main__":
    # 对上面代码进行测试
    logger = GetLogger().get_logger()

    # 在具体需要的地方
    logger.info('INFO日志打印...')
    logger.error('ERROR日志打印...')

    # # 打印日志保存路径
    # sep = os.sep
    # set_log_path = os.path.abspath(
    #     os.path.join(__file__, f"..{sep}..{sep}logs{sep}"))
    # print('测试Log路径：', set_log_path)

    import time

    while True:
        logger.info('每隔X打印一下')
        time.sleep(2)
