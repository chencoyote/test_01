#!/usr/bin/python
import urllib2

f=open("path.txt","r")
paths=f.readlines() #kill \n
paths_2=[]
f.close()

proxyserver=['daili.com','xx.xx','xx.xx','xx.xx']

try:
	for proxy in proxyserver:
        proxy_hadnler=urllib2.ProxyHandler({'http':proxy})
        opener=urllib2.build_opener(proxy_hadnler,urllib2.HTTPHandler)
        #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        #
        try:
        for path in paths:
    	    if path not in paths_2:
    		    path=path.replace("\n",'')
    		    print path 
    		    paths_2.append(path)
    		    response=opener.open(url+,timeout=3)
    		    print response.code
    	    else:
    		    pass
        except urllib2.HTTPError,e:
    	    print e 
        finally:
    	    if response:
    		    response.close()
except Exception,e:
	print e
	pass








