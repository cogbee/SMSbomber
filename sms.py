#coding=utf-8
#!/usr/bin/python
'''
author:jaffer tsao
time:2015-3-29

'''

import httplib2
import urllib  
import threadpool

class sendsms(object):
	def __init__(self,phone,num):
		self.phone = phone
		self.url = 'http://open.epicc.com.cn/eplatform/loginRegister/register/saveYZM'
		self.threadnum = 5
		self.all = num

	def sends(self):
		h = httplib2.Http()
		body = {'mobile': self.phone} 
		headers = {'Content-type': 'application/x-www-form-urlencoded','Origin':'http://open.epicc.com.cn','Referer':'http://open.epicc.com.cn/eplatform/views/loginRegister/register.jsp','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
		'Cookie':'epicc_tid=10.130.67.33.1427628209097650; s_nr=1427630306223-New; _gscu_321070471=27628260i49hyf19; _gscu_793357708=27630350n6xe0314; _gscs_793357708=27640823gjn62i14|pv:1; _gscbrs_793357708=1; EcutH7WVc8=MDAwM2IyYWQzNzQwMDAwMDAwMDIwZjBEBQcxNDI3NjUwMzMx; VwS0QvsNPc=MDAwM2IyYWQ0ZjQwMDAwMDAwM2IwHGpvO0MxNDI3NjUyMjgz; JSESSIONID=2fyQVYSPRLX5cRsD8ZfKCzTmD9phjh83XnJYhJJRMnnH2GYyR1Tl!-731644981'}  
		res,con = h.request(self.url,'POST',headers = headers,body=urllib.urlencode(body))
		print con

	def gothread(self):
		#建立进程池
		pool = threadpool.ThreadPool(self.threadnum)
		#print type(self.threadnum)
		#print self.threadnum
		#两个list合并，直接相加就可以
		for i in range(self.all):
			pool.add_task(self.sends)
		#join and destroy all threads
		pool.destroy()

if __name__=='__main__':
	phone = raw_input('please input a phone:\n')
	num = raw_input('please input the number of sms you want to send\n')
	test = sendsms(phone,num)
	test.gothread()
	raw_input('OK\n')


