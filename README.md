# SeeYou-Platform

![Build](https://img.shields.io/badge/Build-passing-brightgreen.svg)
![Languages](https://img.shields.io/badge/Languages-Python3.6.5-blue)
![Contributions](https://img.shields.io/badge/Contributions-welcome-ff69b4.svg)

## Ⅰ. SeeYou平台简介

### 背景

「SeeYou平台」是一个由「软件测试 & 机器学习爱好者」开发的接口自动化测试平台。

### 愿景

 平台致力于将人工智能技术与软件测试有效结合，让平台在保障测试精确性要求的同时更具智能化、泛化能力，
 同时尽可能 **最优化使用体验** ，目标是成为 **最贴心、最好用、颜值最高** 的开源测试平台。
 
### 技术栈

 平台遵循「前后端分离开发」思想，技术栈为：「Python + Vue + Mongodb」，后端开发使用的是轻量级 Web 框架 Flask，
前端 UI 框架则采用的是易上手的 ElementUi。
 
 [（在这里感谢一下本开源项目给我带来的启发)](https://github.com/githublitao/api_automation_test) 

### 使用环境

**推荐使用 Chrome 最新浏览器使用~**

    
## Ⅱ. SeeYou平台特点 （os：和其他测试平台有什么区别？）
 
  **0.已经投入生产环境使用 1 年以上, 用起来轻松没负担~** 

 1.平台遵循「小而精」的策略，最大化所有功能的开发、使用性价比，可帮助测试团队快速搭建起易于上手 / 维护的接口
 自动化测试体系。
 
 2.平台遵循「零编码」原则，使用者不需要编程即可完成较为复杂的业务流程接口测试。
 
 3.平台遵循「颜值即正义」原则，操作界面展示如下：
 
 ![输入图片说明](https://images.gitee.com/uploads/images/2019/0819/233943_1f8c3f85_5239689.png "操作界面展示.png")
 
 4.平台拥有极佳的定时任务体验，启动定时任务后可随时停用 / 任意编辑任务内容且立即生效，同时拥有丰富的告警策略，
 页面展示如下：
 
 ![输入图片说明](https://images.gitee.com/uploads/images/2019/0819/234004_623ff92c_5239689.png "定时任务配置.png")
 
 5.平台拥有导入 / 导出功能，支持测试人员 **"最喜爱的"** Excel 格式，易于批量生成 / 修改用例。
 
 ![输入图片说明](https://images.gitee.com/uploads/images/2019/0819/234019_f62ca3cb_5239689.png "数据导入展示.png")
 
 6.平台拥有较为丰富的测试结果校验体系，支持**文本相似度**校验。
 ([具体内容可参考本篇博文](https://juejin.im/post/5cfe1dd96fb9a07ed7407321))
 
 7.平台对外提供测试任务调度接口，方便与开发项目集成。
 
 8.......
 
 ***（还有许许多多令人惊喜的小特色等着你去探索 & 挖掘）***
 

## Ⅲ .SeeYou平台功能图解

### V1.0

![输入图片说明](https://images.gitee.com/uploads/images/2019/0819/234034_604458dd_5239689.png "SeeYou平台结构图_V1.0.png")


## IV . SeeYou平台部署

### windows 环境下部署

#### 0. 克隆项目

    git clone https://gitee.com/amazingTest/Taisite-Platform.git

#### 1. 安装 python 3 环境

[点击进入python教程](https://www.runoob.com/python3/python3-install.html)

[建议：Ptyhon项目单独创建虚拟环境](https://shimo.im/docs/yRjCrCkXq3xpydGg)

#### 2. 部署自然语言模型

[点击下载模型](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)

2.2 解压压缩包

2.3 安装 python 依赖包

    pip install tensorflow==1.14.0  -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install bert-serving-server==1.9.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
  
2.4 启动模型

    // 当前目录切换至模型文件夹目录后执行
    bert-serving-start -model_dir ./chinese_L-12_H-768_A-12/ -num_worker=1
  
启动成功后输出如下：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132542_87013872_5239689.png "NLP模型启动成功输出.png")

#### 3. 部署 Mongodb 数据库

[点击进入教程](https://www.runoob.com/mongodb/mongodb-window-install.html)

#### 4. 设置系统环境变量

    AUTOTEST_PLATFORM_ENV=production
    AUTOTEST_PLATFORM_NLP_SERVER_HOST=127.0.0.1
    AUTOTEST_PLATFORM_MONGO_HOST=${MONGO_HOST}
    AUTOTEST_PLATFORM_MONGO_PORT=${MONGO_PORT}
    AUTOTEST_PLATFORM_MONGO_USERNAME=${USERNAME}
    AUTOTEST_PLATFORM_MONGO_PASSWORD=${PASSWORD}
    AUTOTEST_PLATFORM_MONGO_DEFAULT_DBNAME=taisite
  
其中 AUTOTEST_PLATFORM_ENV 默认为 production （必填）

AUTOTEST_PLATFORM_MONGO_HOST和 AUTOTEST_PLATFORM_MONGO_PORT 分别表示数据库的地址和端口（必填）

AUTOTEST_PLATFORM_MONGO_USERNAME和 AUTOTEST_PLATFORM_MONGO_PASSWORD 分别表示数据库的帐号密码（若无可不填）

AUTOTEST_PLATFORM_NLP_SERVER_HOST（自然语言模型服务）默认为本机启动 （非必填）

AUTOTEST_PLATFORM_MONGO_DEFAULT_DBNAME 为默认的数据表名（必填）

设置完成后可通过下列命令进行测试（CMD切换至项目根目录下）

    python ./backend/config.py
  
若配置成功则可看见输入的配置数据

#### 5. 打包前端 dist 文件 （这一步我已为你们做好，若不需二次开发可跳过）

5.1 安装 Vue 环境，下载 node.js 并配置环境，下载 npm 包管理器

5.2 cmd 进入 frontend 目录下，配置 cnpm :

    npm install -g cnpm --registry=https://registry.npm.taobao.org   
  
5.3 执行安装依赖包命令:

    cnpm install
  
5.4 执行打包命令:

    cnpm run build
  
若成功打包则会在项目根目录下生成 dist 文件夹。


TODO 部署时不需要可直接跳过
> one. 给项目添加 favicon.ico  https://www.jianshu.com/p/1f7a096b61c2
> two. vue项目中 favicon.ico不能正确显示的问题 https://www.jianshu.com/p/980cb1caf7a8
> three. 修改index.js的icon  http://www.fontawesome.com.cn/faicons/

#### 6. 启动后端

    // 安装依赖包 (切换至项目根目录下执行)
    pip install -r ./backend/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

    // 启动后端 ( 默认5050端口 )
    python ./backend/run.py

    // 创建平台管理员帐号密码
    python ./backend/createAdminUser.py
  
#### 7. 访问项目

现在就可以访问 http://127.0.0.1:5050/#/login 使用创建的管理员帐号密码进行登录。






### Linux 环境下 Docker 容器化部署

[点击进入 Docker 教程地址](https://www.runoob.com/docker/ubuntu-docker-install.html)

#### 0. 克隆项目

    git clone https://gitee.com/amazingTest/Taisite-Platform.git
  
#### 1. 自然语言模型部署

    sudo -i
    docker pull shaoyuyishiwo/bertserver
    docker run --name autotest-platform-bertserver -d shaoyuyishiwo/bertserver 


#### 2. Mongo 数据库部署 (若已有现成数据库可用则可跳过此步)

2.1 启动数据库 & 数据挂载至宿主机

    sudo -i
    docker pull mongo 
    docker run  --name autotest-platform-mongo -p 27017:27017 -v /data/db:/data/db -v /data/configdb:/data/configdb ``-d mongo
  
2.2 创建数据库帐号

    docker exec -it autotest-platform-mongo /bin/bash

    mongo

    > use admin

    switched to db admin

    > db.createUser({user:"${USERNAME}",pwd:"${PASSWORD}",roles:["root"]})

    Successfully added user: { "user" : "admin", "roles" : [ "root" ] }
  
2.3 数据库内存扩容(建议)

    > db.adminCommand({setParameter:1, internalQueryExecMaxBlockingSortBytes:335544320})

    { "was" : 33554432, "ok" : 1 }
  
#### 3. 环境变量配置

    // 编辑 /etc/profile 文件

    sudo -i
    vi /etc/profile
  
若出现警告则选择 (E)dit anyway (输入 E)

3.1 文本末端插入下列数据 (输入 i 则变为 insert 状态)

    export AUTOTEST_PLATFORM_ENV=production
    export AUTOTEST_PLATFORM_NLP_SERVER_HOST=${BERT_IPADRESS}
    export AUTOTEST_PLATFORM_MONGO_HOST=${MONGO_HOST}
    export AUTOTEST_PLATFORM_MONGO_PORT=${MONGO_PORT}
    export AUTOTEST_PLATFORM_MONGO_USERNAME=${USERNAME}
    export AUTOTEST_PLATFORM_MONGO_PASSWORD=${PASSWORD}
    export AUTOTEST_PLATFORM_MONGO_DEFAULT_DBNAME=${DBNAME}

变量为动态值，部署者自行根据实际情况输入，DBNAME 值可任意自定义（数据库表名），其中 BERT_IPADRESS 和 MONGO_HOST 值可通过下列命令查询：

    docker inspect autotest-platform-bertserver
    docker inspect autotest-platform-mongo // 若使用了上面的步骤部署数据库
  
输出如下图所示：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132621_3c98dfce_5239689.png "控制台输出1.png")

3.2 插入完毕后点击 ESC 按钮、输入 :wq 后单击回车保存

3.3 执行下列命令后环境变量立即生效

    source /etc/profile
  
#### 4. 启动项目

//在项目根目录下执行部署文件

    sh deploy ${PORT} 
  
其中 ${PORT} 变量填写项目访问端口即可，项目启动的同时也创建了管理员帐号密码，如下图所示：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132633_79db1be5_5239689.png "控制台输出2.png")

#### 5. 访问项目

浏览器访问部署服务器地址的 ${PORT}端口即可



### Docker 部署python项目补充

1. 安装docker compose
2. 新建 docker-compose.yml 文件
3. docker-compose up 启动
   docker-compose up -d 后台启动

参考：
1. https://www.runoob.com/docker/docker-compose.html
2. https://blog.csdn.net/weixin_34064653/article/details/91923102



#### EXTRA. 常见问题

下列输出代表 **NLP模型** 启动失败

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132647_0cc626a2_5239689.png "NLP部署失败.png")

解决步骤：

1.删除 ./backend/app/init.py 中的这段代码：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132654_00c14401_5239689.png "不使用NLP模型方法指南1.png")

2.将 ./backend/testframe/interfaceTest/tester.py 中的下列代码修改成 pass：

![输入图片说明](https://images.gitee.com/uploads/images/2019/0907/132701_3dfea6a4_5239689.png "不使用NLP模型方法指南2.png")

完成后再启动项目时，就不会依赖于自然语言模型了~

## V . SeeYou平台使用教程

平台主流程使用可参考[本篇博文中的正文部分](https://juejin.im/post/5cd0117be51d456e537ef3bd)


## linux-CentOS7 不适用docker部署项目


1. 将项目代码克隆到linux，git clone https://github.com/Valuebai/SeeYou-Platform.git
2. 安装python环境，本项目使用python3.6.5
3. 安装pip包，pip install -r requirements.txt
4. 安装mongodb，[CentOS7.4 安装mongodb](https://www.jianshu.com/p/994bc7b19b26) ，用里面不用授权的
5. 创建登录账号
- 使用脚本：进入./backend/，执行python createAdminUser.py
- 直接创建：在mongodb创建【待补充】
6. 运行项目看效果，进入./backend/，执行python run.py 
7. 项目运行正常，linux上可使用下面的命令让其在后台运行
- # linux 上需要先安装gunicorn -->> pip3 install gunicorn
 sh run.sh 或者 . run.sh 运行
```
run.sh内容
# shell杀死指定端口的进程，写到部署脚本里面
kill -9 $(netstat -nlp | grep :5050 | awk '{print $7}' | awk -F"/" '{ print $1 }')

# 另一个启动方式nohup python3 -u  run.py > nohup.log 2>&1 &
# 后台运行
nohup gunicorn -w 4 -b 0.0.0.0:5050 run:app > gunicorn.log 2>&1 &
```

开启服务器对应5050端口
firewall-cmd --zone=public --add-port=5050/tcp --permanent 永久开启5050端口
firewall-cmd --reload #重启firewall 每次新添加端口都要
> 参考：[【Linux】CentOS-常用命令&新购买云服务器安装必看](https://github.com/Valuebai/awesome-python-io/issues/1)

 
### 为Python项目创建独立的虚拟环境（可选）
[python在win/linux创建虚拟环境](https://blog.csdn.net/luhuibo318/article/details/94011917)


### 新购买的linux-CentOS7 云服务器部署指南
1. [【Linux】CentOS-常用命令&新购买云服务器安装必看](https://github.com/Valuebai/awesome-python-io/issues/1)
2. [总结python+flask项目在linux部署的五大方法](https://blog.csdn.net/luhuibo318/article/details/102688154)