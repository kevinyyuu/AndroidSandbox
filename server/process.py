#-*- coding: utf-8 -*-

'''
这个模块负责apk的自动化处理，通过schedule模块开启一个线程调用，
模块内调用为：prepare --> adb --> display
'''

import log, display, prepare
from database import datab

class Process:
    '''
    该类中包含了对一个任务的完整处理流程，
    由schedule模块可以对该类进行实例化和start
    '''

    def __init__(self):
        pass

    def start(self):
        pass

    def creat_virtual_machine(self):
        pass

    def install_apk(self):
        pass

    def prepare_apk(self):
        pass

    def catch_log(self):
        pass

    def display_log_html(self):
        pass