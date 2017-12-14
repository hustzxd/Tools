#### Usage

[caffe draw figures](http://blog.csdn.net/u013078356/article/details/51154847)

```sh
#!/usr/bin/env sh
set -e
HOME=/home/zhaoxiandong/
TOOLS=$HOME/caffe/build/tools
GLOG_logtostderr=0 GLOG_log_dir=log/ \
$TOOLS/caffe train \
    --solver=$1 \
    --weights=$2 \
    --gpu=3
```

`./parse_log.sh caffe.wujiyang-ubuntu.wujiyang.log`

After that, you can get *.test *.train

`./plot_training_log.py.example 0  save.png caffe.wujiyang-ubuntu.wujiyang.log`

```
Notes:  
    1. Supporting multiple logs.  
    2. Log file name must end with the lower-cased ".log".  
Supported chart types:  
    0: Test accuracy  vs. Iters  
    1: Test accuracy  vs. Seconds  
    2: Test loss  vs. Iters  
    3: Test loss  vs. Seconds  
    4: Train learning rate  vs. Iters  
    5: Train learning rate  vs. Seconds  
    6: Train loss  vs. Iters  
    7: Train loss  vs. Seconds
```

But sometimes you can't run this command on server.

So you can try:

`python plot_figures.py led.log.test`