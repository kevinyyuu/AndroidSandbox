#-*- coding: utf-8 -*-

'''
该模块用于数据库处理
'''

import sqlite3, os

class Datab:
    '''
    处理数据库
    调用样例：datab.sql
    '''

    def __init__(self):
        self.connect_to_datab()

    def connect_to_datab(self):
        path = os.getcwd()
        pparent_path = os.path.dirname(path)
        data_path = os.path.join(pparent_path, 'data', 'data.db')
        print(data_path)
        self.sql = sqlite3.connect(data_path)

    def query_maxtask_id(self):
        '''
        查询数据库最大任务id
        :return: id编号
        '''
        pass

    def query_propare_id(self, id):
        '''
        查询数据库中指定id的apk文件是否已经预处理完成
        :param id: 待查询任务id
        :return: 处理状态
        '''
        pass

    def query_handle_id(self, id):
        '''
        查询数据库中指定id的任务是否已经分析完成
        :param id: 待查询任务id
        :return: 处理状态
        '''
        pass

    def change_propare_id(self, id):
        '''
        更改数据库中指定任务的预处理状态
        :param id: 待更改任务id
        :return: 无
        '''
        pass

    def change_handle_id(self, id):
        '''
        更改数据库中指定任务的分析状态
        :param id: 待更改任务id
        :return: 无
        '''
        pass


datab = Datab()