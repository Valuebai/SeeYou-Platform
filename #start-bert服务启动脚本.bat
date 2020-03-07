rem 这个脚本放到与模型文件夹同级目录执行
:: 需要安装 python 依赖包
:: pip install tensorflow==1.14.0  -i https://pypi.tuna.tsinghua.edu.cn/simple
:: pip install bert-serving-server==1.9.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

bert-serving-start -model_dir ./chinese_L-12_H-768_A-12/ -num_worker=1

pause