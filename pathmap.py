#!/usr/bin/python 
# -*- coding: utf-8 -*-          
import httplib
import sys

headers={}
headers['user-agent']="Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"
#referer

#打开文件，将文本写入数组          
def passlist(): 
    try:
        f=open('path.txt','r')
        lib=f.readlines()
        f.close()
        return lib
    except:
        print "this is no path.txt"
        pass

#测试不存在的页面_返回码
def no_path(http_address):
    #test_url="/fuckyoufuckyoufuckyou.html"
    test_path="/fuckyoufuckyoufuckyou"
    conn=httplib.HTTPConnection(http_address)
    conn.request("HEAD",test_path)
    return conn.getresponse().status
    conn.close
#测试不存在的页面_返回页面长度

#扫描路径 
 
def test_http_head(http_address,lib,no):
    ''' lib为存放路径的数组,no测试的不存在页面返回码 '''
    #f=open('path.txt','r')
    #lib=f.readlines()
    conn=httplib.HTTPConnection(http_address) 
    #conn.set_debuglevel(1) 
    for path in lib:   
        path = path.replace("\n","")
        print path
        #conn.set_debuglevel(2)
        conn.request('HEAD',path)  #headers=headers   
        #print conn.getresponse().status
        status_test=str(conn.getresponse().status)
        if status_test==str(no):
            pass
        else:
            print  status_test
        conn.close()   #位置问题 
#多线程实现 
if __name__=="__main__":
    http_address=sys.argv[1]
    try:
        lib=passlist() #文本写入数组
    except:
        pass
    try: 
        no=no_path(http_address)
        test_http_head(http_address,lib,no)
    except KeyboardInterrupt:
        print "Scan done\n"
    
   
