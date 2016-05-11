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
        self.current_id = -1
        self.current_thread = []
        mailbox = transimitter.Communication()
        threading.Thread(target=mailbox.start()).start()

    def check_new_task(self):
        if(datab.query_maxtask_id() > self.current_id):
            return self.current_id+1
        return 0

    def check_finish_task(self):
        return datab.query_handle_id(self.current_id)

    def creat_new_task(self):
        if(self.current_thread.is_alive() == False):
            pass

    def send_html_back(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

if(__name__ == '__main__'):
    envir = Envir()
    envir.start()
