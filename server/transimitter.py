#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
该模块用于与客户端的通信，当接收到客户端请求时，保存apk文件到/data目录
同时增加一个数据库条目，线程内还会检查下一个将处理的apk条目是否已经处理完成，
检查到handle_flag为true时便回发给客户端
'''

import socket, os, re, time
from database import datab

class Communication:
    '''
    负责与客户端通信
    '''

    def __init__(self):
        com = 9999
        addr = '127.0.0.1'
        self.connection = []
        self.current_path = ''
        self.current_name = ''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((addr, com))
        self.sock.listen(1)

    def send_html_back(self):
        '''
        通过connection连接发送文件到服务器
        :param connection: socket套接字
        :param filename: 待发送文件
        :return: 无
        '''
        filename = os.path.join(self.current_path, self.current_name)
        filename += '.html'
        f = open(filename, 'rb')
        print('Sending html result file...')
        while(True):
            data = f.read(4096)
            if(not data):
                break
            self.connection.sendall(data)
        f.close()
        time.sleep(1)
        self.connection.sendall('EOF'.encode('utf-8'))
        print('HTML result file success send!')

    def rev_apk(self, name):
        '''
        接收客户端发送的文件
        :param name: 客户端发送的apk文件名
        :return: 无
        '''
        parent_path = os.path.dirname(os.getcwd())
        file_path = os.path.join(parent_path, 'data')
        file_path = os.path.join(file_path, name)
        while(os.path.exists(file_path)):
            file_path += '_'
        os.mkdir(file_path)
        self.current_path = file_path       #保存当前文件目录
        file = os.path.join(file_path, name+'.apk')
        f = open(file, 'wb')
        print('Receiving apk file...')
        while(True):
            data = self.connection.recv(4096)
            if(data == 'EOF'.encode('utf-8')):
                print('Recv file success!')
                break
            f.write(data)
        f.close()

    def get_apk_name(self, filename):
        '''
        利用正则表达式获取文件名
        :param filename:
        :return:
        '''
        p = re.compile(r"/?([^/]*).apk")
        data = p.findall(filename)
        return data[0]

    def start(self):
        '''
        接收一个客户端请求并建立连接，
        解析客户端请求
        :return: 无
        '''
        while(True):
            self.connection, address = self.sock.accept()
            print('Connection established')
            self.connection.send('Welcome to Android Sandbox!\n'.encode('utf-8'))
            while(True):
                buf = self.connection.recv(1024).decode('utf-8')    #接收客户端请求
                if(buf[0:2] == 'RS'):                               #客户端请求发送文件
                    self.connection.send('AC'.encode('utf-8'))
                    self.current_name = self.get_apk_name(buf[3:])
                    self.rev_apk(self.current_name)                 #服务器接收apk文件
                    self.connection.send('RS'.encode('utf-8'))      #服务器请求发送html结果文件
                    temp = self.connection.recv(1024).decode('utf-8')
                    if(temp == 'AC'):                   #服务器被允许发送结果文件
                        self.send_html_back()           #服务器开始发送结果文件
                elif(buf == 'quit'):
                    break
                else:
                    self.connection.send('ERROR! unrecognized command!\n'.encode('utf-8'))
            self.connection.close()
