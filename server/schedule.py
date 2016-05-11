#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
该模块用于任务调度，其通过不断检查数据库，发现新任务便开启虚拟机快照，
同时开启process模块线程，对当前任务处理
'''

import threading, time, transimitter
from database import datab

class Envir:
    '''
    运行环境底层
    '''

    def __init__(self):
        self.current_id = datab.query_maxtask_id()
        self.current_thread = []
        self.tran = transimitter.Communication()
        t = threading.Thread(target=self.tran.start)
        t.setDaemon(True)
        t.start()

    def check_new_task(self):
        if(datab.query_maxtask_id() > self.current_id):
            return self.current_id+1
        return -1

    def check_finish_task(self):
        return datab.query_handle_id(self.current_id)

    def creat_new_task(self):
        pass

    def send_html(self):
        self.tran.right_to_html = True

    def start(self):
        while(True):
            flag = self.check_new_task()       #检查是否有新的任务
            if(flag != -1):
                self.current_id = flag
                self.creat_new_task()
                while(True):            #等待服务器处理完成
                    if(datab.query_handle_id(self.current_id)):
                        self.send_html()
                    time.sleep(0.5)
            time.sleep(0.5)

    def stop(self):
        pass

envir = Envir()
while(True):
    envir.start()