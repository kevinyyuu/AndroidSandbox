# -*- coding: utf-8 -*-

import socket, time, re

def send_file(connection, filename):
    '''
    通过connection连接发送文件到服务器
    :param connection: socket套接字
    :param filename: 待发送文件
    :return: 无
    '''
    f = open(filename, 'rb')
    print('Sending apk file...')
    while(True):
        data = f.read(4096)
        if(not data):
            break
        connection.sendall(data)
    f.close()
    time.sleep(1)
    connection.sendall('EOF'.encode('utf-8'))
    print('File success send!')

def recv_file(connection, filename):
    '''
    接收服务器发送的结果文件
    :param connection:
    :param filename:
    :return:
    '''
    print('Receiving html file...')
    name = get_apk_name(filename)
    file = name + '.html'
    f = open(file, 'wb')
    while(True):
        data = connection.recv(4096)
        if(data == 'EOF'.encode('utf-8')):
            print('Recv HTML result file success!')
            break
        f.write(data)
    f.close()

def get_apk_name(filename):
    '''
    利用正则表达式获取文件名
    :param filename:
    :return:
    '''
    p = re.compile(r"/?([^/]*).apk")
    data = p.findall(filename)
    return data[0]

com = 9999
addr = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr, com))
print(sock.recv(1024).decode('utf-8'))
while(True):
    command = input('command: ')
    if(command == 'quit'):                      #客户端申请退出
        sock.send('quit'.encode('utf-8'))
        break
    elif(command[0:2] == 'RS'):
        sock.send(command.encode('utf-8'))      #客户端请求发送apk文件
        recv = sock.recv(1024).decode('utf-8')
        if(recv == 'AC'):                       #服务器同意客户端发送请求
            send_file(sock, command[3:])
            if(sock.recv(1024).decode('utf-8') == 'RS'):    #服务器请求发送结果文件
                sock.send('AC'.encode('utf-8'))             #客户端允许服务器发送文件
                recv_file(sock, command[3:])                #客户端开始接收文件
        else:
            print('The server didn`t allow you to send.')
    else:
        print('Wrong input!')
sock.close()

