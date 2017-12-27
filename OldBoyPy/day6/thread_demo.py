#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from threading import Thread
import time


class My_thread(Thread):
    # 子定义 Thread子类，重置run函数方法
    def run(self):
        print('my_thread')
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs


def foo(arg):
    print(arg)
    for j in range(10):
        # print(arg)
        print(j)
        time.sleep(1)


print('before')
for i in range(10):
    # 创建实例，并执行函数
    t_i = Thread(target=foo, args=(i,))
    # 设置isDaemon为true
    # t_i.setDaemon(True)
    # 开始执行
    t_i.start()
    # join() 等待线程完成。顺序执行，参数timeout 表示等待的时间，默认为空
    # t_i.join()
    # 获取线程名称 , 和isDaemon，false表示等待子进程结束，true不等待
    print(t_i.getName(), t_i.isDaemon())
# 创建自定义my_thread 实例，调用执行run函数
t2 = My_thread(target=foo, args=(1,))
t2.start()
print('after')
