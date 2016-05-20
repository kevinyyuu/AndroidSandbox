#-*- coding: utf-8 -*-

'''
python 2.7下调试  需要修改
这个模块负责apk的自动化处理，通过schedule模块开启一个线程调用，
模块内调用为：prepare --> adb --> display
'''
'''
APK文件需放在adb目录下
需要安装adb voxmanage以及import载入的部分包
需要vboxmanage环境变量 adb环境变量
'''

# import log, display, prepare
import os
import time
import commands
import traceback
#from database import datab
from multiprocessing import Process

name=['test1.apk','test.apk','test2.apk']

class Process:
    '''
    该类中包含了对一个任务的完整处理流程，
    由schedule模块可以对该类进行实例化和start
    '''

    def __init__(self):
        pass
    '''
        main_process=Process(target=creat_virtual_machine)
        main_process.start()
    '''

    def start(self):
        print 'start ........'

    def creat_virtual_machine(self):
        #os.system(cd_menu)  #VBoxManage list vms  "Android" {1ab9f042-db9e-4616-8fe0-e5c4ae5a0a4e}
        os.system('VBoxManage startvm Android')
        os.system('VBoxManage list runningvms')
        print 'wait for 50s'
        time.sleep(50)
        print 'start to adb'
        os.system('adb kill-server')
        os.system('adb start-server')
        #os.system('adb shell')
        #os.system('exit')
        
    def prepare_apk(self):
        #将apk文件移至adb目录下
        pass

    def install_apk(self,apk_name,id):
        #(status,) = commands.getstatusoutput('adb install '+name[id])
        print 'install '+apk_name[id]
        status=os.system('adb install '+apk_name[id])
        return status

    def unistall_apk(slef):
        os.system('adb shell su')

        #q前面全部调试完成 可以使用 后面仍有问题
        os.system('cd data/app')
        (status,out) = commands.getstatusoutput('ls')
        package_name_name='uninstall '+out
        status=os.system('adb uninstall '+package_name)
        return status

    def pause_statue(self,num)
        os.system('VBoxManage snapshot Android'+'pause_statue'+num)


    def catch_log(self):
        pass

    def display_log_html(self):
        pass
     
    def end_all(self):
        os.system('VBoxManage controlvm Android acpipowerbutton')
        
if __name__ == "__main__":
    one=Process()
    one.start()
    one.creat_virtual_machine()
    try:
        one.install_apk(name,1)
    except:
        print 'error'
        f=open('1.txt','a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()
    time.sleep(20)   #等待程序安装完毕 可由相关线程通过判断install_apk的返回值来确定
    one.unistall_apk()
    






