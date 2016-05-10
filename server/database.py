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
        self.cur = self.sql.cursor()

    def connect_to_datab(self):
        path = os.getcwd()
        pparent_path = os.path.dirname(path)
        data_path = os.path.join(pparent_path, 'data', 'data.db')
        self.sql = sqlite3.connect(data_path)

    def query_maxtask_id(self):
        '''
        查询数据库最大任务id
        :return: id编号
        '''
        data = self.cur.execute('SELECT * FROM apk')
        max_id = len(data.fetchall())
        return max_id

    #三种查询方法
    def query_name_id(self, id):
        return self.query_sql(id, 'name')

    def query_prepare_id(self, id):
        '''
        查询数据库中指定id的apk文件是否已经预处理完成
        :param id: 待查询任务id
        :return: 处理状态
        '''
        return self.query_sql(id, 'prepare')

    def query_handle_id(self, id):
        '''
        查询数据库中指定id的任务是否已经分析完成
        :param id: 待查询任务id
        :return: 处理状态
        '''
        return self.query_sql(id, 'handle')

    def query_sql(self, id, type):
        column = 3
        if(type == 'prepare'):
            column = 2
        elif(type == 'handle'):
            column = 3
        elif(type == 'name'):
            column = 1
        data = self.cur.execute('SELECT * FROM apk WHERE id = ' + str(id))
        ans = data.fetchall()[0][column]
        return ans

    def change_propare_id(self, id, state):
        '''
        更改数据库中指定任务的预处理状态
        :param id: 待更改任务id
        :return: 无
        '''
        self.cur.execute('UPDATE apk SET pre_flag = '+ str(state) + ' WHERE id = ' + str(id))

    def change_handle_id(self, id, state):
        '''
        更改数据库中指定任务的分析状态
        :param id: 待更改任务id
        :return: 无
        '''
        self.cur.execute('UPDATE apk SET handle_flag = '+ str(state) + ' WHERE id = ' + str(id))

    def add_task(self, name):
        '''
        添加一个新的任务
        :param name:
        :return:
        '''
        self.cur.execute('INSERT INTO apk VALUES (NULL, "%s", 0, 0)' % name)
        self.sql.commit()

datab = Datab()

if(__name__ == '__main__'):
    num = datab.query_maxtask_id()
    prepare_state = datab.query_prepare_id(1)
    handle_state = datab.query_handle_id(1)
    name = datab.query_name_id(1)
    datab.change_propare_id(1, 0)
    datab.change_handle_id(1, 1)
    prepare_state = datab.query_prepare_id(1)
    handle_state = datab.query_handle_id(1)
    datab.add_task('test')
    print(prepare_state, handle_state, name)