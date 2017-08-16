# -*- coding: UTF-8 -*-
'''
Created on Aug 7, 2017

@author: zhaxind
'''

import requests
from lxml import html
import re
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#First task
#===============================================================================
# page = requests.get("http://www.heibanke.com/lesson/crawler_ex00")
# 
# tree = html.fromstring(page.text)
# 
# task_string = tree.xpath('//h3/text()')
# digitP = re.compile('\D*([0-9]+)\D*')
# m=digitP.match(str(task_string))
# 
# while(m):
#     print(m.group(1))
#     requestString = "http://www.heibanke.com/lesson/crawler_ex00/" + str(m.group(1))
#     page=requests.get(requestString)
#     tree = html.fromstring(page.text)
#     task_string = tree.xpath('//h3/text()')
#     m = digitP.match(str(task_string))
#     print(task_string)
#     sleep(3)
#===============================================================================
#Key number 57633 

# page = requests.get("http://www.heibanke.com/lesson/crawler_ex01/")

# browser = webdriver.Chrome(executable_path='C:/Users/zhaxind/eclipse-workspace/SpiderVPN/Dirver/chromedriver.exe')
# browser.get('http://www.baidu.com/')

# driver = webdriver.Chrome(executable_path='C:/Users/zhaxind/eclipse-workspace/SpiderVPN/Dirver/chromedriver.exe')
# driver.get("http://www.heibanke.com/lesson/crawler_ex01/")
# username = driver.find_element_by_xpath('//form/*[2]/input')
# passowrd = driver.find_element_by_id('id_password')
# login= driver.find_element_by_id('id_submit')
# i=0
# result = driver.find_element_by_xpath('//h3').text
# print(result)
# 
# username.send_keys("xinduo")
# passowrd.send_keys(i)
# login.click()
# 
# wait = WebDriverWait(driver, 10)
# 
# wait.until_not(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'h3'),''))
# 
# result = driver.find_element_by_xpath('//h3').text
# 
# while(result=='您输入的密码错误, 请重新输入'):
#     i=i+1
#     driver.execute_script("window.history.go(-1)")
#     wait.until(EC.element_to_be_clickable((By.ID,'id_password')))
#     passowrd = driver.find_element_by_id('id_password')
#     login= driver.find_element_by_id('id_submit')
#     passowrd.send_keys(i)
#     login.click()
#     
# print(result)
#     
# postData = {'username':'xinduo','password':1}
# r=requests.post("http://www.heibanke.com/lesson/crawler_ex01/",data=postData)
# print(r.text)

#Second task
#===============================================================================
# url = "http://www.heibanke.com/lesson/crawler_ex01/"
# r=requests.get(url)
# cookieString=''
# for key, value in r.cookies.items():
#     cookieString = (key + '=' + value+';')
# print(cookieString)
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookieString.split(';'):
#     if cookie!='':
#         key,value = cookie.split('=',1)
#         jar.set(key,value)
#  
# for x in range(0, 31):
#     postData = {'username':'xinduo','password':x}
#     r=requests.post(url,data=postData,cookies=jar)
#     failP = re.compile('密码错误')
#     if not (failP.search(r.text)) :
#         print("password is "+ str(x))
#         print(r.text)
#         break
#===============================================================================
#Password is 22    

#Third task
#===============================================================================
# s = requests.session()
# url = "http://www.heibanke.com/lesson/crawler_ex02/"
# r1=s.get(url)
# cookieString=''
# for key, value in r1.cookies.items():
#     cookieString = (key + '=' + value+';')
# print(cookieString)
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookieString.split(';'):
#     if cookie!='':
#         key,value = cookie.split('=',1)
#         jar.set(key,value)
# 
# postData={'username':'xinduo','password':'q1w2e3r4','csrfmiddlewaretoken':jar.get("csrftoken")}
# r2=s.post(r1.url,data=postData,cookies=jar)
# 
# for x in range(0, 31):
#     postData = {'username':'xinduo','password':x,'csrfmiddlewaretoken':jar.get("csrftoken")}
#     r=s.post(url,data=postData,cookies=jar)
#     failP = re.compile('密码错误')
#     if not (failP.search(r.text)) :
#         print("password is "+ str(x))
#         print(r.text)
#         break
#===============================================================================
#Password is 28


s = requests.session()
url = "http://www.heibanke.com/lesson/crawler_ex03"
r1=s.get(url)
cookieString=''
for key, value in r1.cookies.items():
    cookieString = (key + '=' + value+';')
#print(cookieString)
jar = requests.cookies.RequestsCookieJar()
for cookie in cookieString.split(';'):
    if cookie!='':
        key,value = cookie.split('=',1)
        jar.set(key,value)
 
postData={'username':'xinduo','password':'q1w2e3r4','csrfmiddlewaretoken':jar.get("csrftoken")}
r2=s.post(r1.url+'/pw_list',data=postData,cookies=jar)

passIndexList = list()
passValueList = list()
password="" 
passDict = dict()

while(len(passDict)!=100):
    for x in range (1,14):
        passListPage={'page':x}
        r3=s.get(url + '/pw_list', params=passListPage)
        failP = re.compile('404 Not Found')
        print(re.findall(r'password_pos">(\d+)', r3.text))
        passIndexList = passIndexList + re.findall(r'password_pos">(\d+)', r3.text)   
        passValueList = passValueList + re.findall(r'password_val">(\d+)', r3.text)
        print('page ' + str(x) + ' has been analyzed')
       
    passDict={**passDict,**dict(zip(passIndexList,passValueList))}
  
for x in range(1,len(passDict)+1) :
     password = password + str(passDict.get(str(x)))

print(password)




