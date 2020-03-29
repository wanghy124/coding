from time import sleep
import time
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
# list = [1, 2]
# for i in tqdm(range(5)):
#    # 模拟你的任务
#    for i in list:
#       print(i)


#total参数设置进度条的总长度
with tqdm(total=100) as pbar:
  for i in range(100):
    time.sleep(0.05)
    #每次更新进度条的长度
    pbar.update(1)