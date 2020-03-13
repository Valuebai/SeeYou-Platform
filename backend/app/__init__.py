#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append('..')
from flask import Flask
from flask_cors import CORS
from utils.mango import *
from config import Config
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__,
            static_folder="../../dist/static",
            template_folder="../../dist")

_config = Config()
app.config['SECRET_KEY'] = _config.get_secret_key()
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。
login_manager = LoginManager()
login_manager.init_app(app)
cors = CORS(app, supports_credentials=True)

conn, db = connect(_config.get_mongo_default_db_name(),
                   ip=_config.get_mongo_host(),
                   port=int(_config.get_mongo_port()),
                   username=_config.get_mongo_username(),
                   password=_config.get_mongo_password())

from utils.cron.cronManager import CronManager

cron_manager = CronManager()
cron_manager.start()

# 如果不需要bert NLP词向量模型
# 1. 将下面4行代码注释掉
# 2. 再将 ./backend/testframe/interfaceTest/tester.py 中的下列代码修改成 pass：
from utils.nlp.Nlper import Nlper
from bert_serving.client import BertClient
bert_ip = _config.get_nlp_server_host() if _config.get_nlp_server_host() else '127.0.0.1'
bert_client = BertClient(ip=bert_ip, timeout=10000)
nlper = Nlper(bert_client)


from models import project, host, caseSuite, testingCase, testReport, cronTab, mail, mailSender

from app.user import user
from app.case import project, host, caseSuite, testingCase, testReport
from app.mail import mail, mailSender
from app.timer import cronTab
from app.notice import webhook