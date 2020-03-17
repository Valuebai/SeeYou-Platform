rem kill the existing process
ps -ef | grep 'bert-serving-start' | grep -v grep | awk '{print $2}' | xargs kill -s SIGINT

rem run bert, need to enter the same root
nohup bert-serving-start -model_dir ./chinese_L-12_H-768_A-12/ -num_worker=1 > bert.log 2>&1 &