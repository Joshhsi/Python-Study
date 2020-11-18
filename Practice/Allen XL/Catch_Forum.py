import urllib
import time
import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy as np
import ssl



username = 'Allen_XL_Li'
password = '10877013'
session = requests.session()

print("*********************************************************************")


#抓登入需要的hash值，Dizcuz分別有loginhash跟forhash
def get_login_window():  
    url='http://10.34.40.113/pcedforum/member.php?mod=logging&action=login&referer=http%3A%2F%2F10.34.40.113%2Fpcedforum%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D2'  
    headers={'Host':'www.discuz.net','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'http://www.discuz.net/forum.php','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-TW,zh;q=0.8'}  
    #清空原来的headers  
    session.headers.clear()  
    #更新headers  
    session.headers.update(headers)  
    r=session.get(url)  
    #获取loginhash  
    p=r.text.find('loginhash')+len('loginhash')+1  
    loginhash=r.text[p:p+5]  
    #获取formhash  
    p=r.text.find('formhash')+len('formhash" value="')  
    formhash=r.text[p:p+8]  
    return (loginhash,formhash) 


#模擬登入
def login(loginhash,formhash,username,password):  
    url='http://10.34.40.111/pcedforum/member.php?mod=logging&action=login&loginsubmit=yes&loginhash='+loginhash
    data={'formhash':formhash,  
        #'referer':'http://www.discuz.net/forum.php',  
        #'loginfield':'username',  
        'username':username,  
        'password':password,  
        #'questionid':'0',  
        #'answer':'',  
        #'seccodehash':'cSA',  
        #'seccodemodid':'member::logging',  
        #'seccodeverify':code
        }  
    headers={'Host':'www.discuz.net','Connection':'keep-alive','Content-Length':'203','Cache-Control':'max-age=0','Origin':'http://www.discuz.net','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36','Content-Type':'application/x-www-form-urlencoded','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Referer':'http://www.discuz.net/forum.php','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-TW,zh;q=0.8'}  
    session.headers.clear()  
    session.headers.update(headers)  
    r=session.post(url,data)  
    print(r.text)
    #輸出結果可以看到登入畫面成功的html檔資訊
    #以下嘗試用request的get功能抓取網頁資料，但是失敗了   
    response = session.get('http://10.34.40.113/pcedforum/forum.php',headers = headers)
    print(response.status_code)
    print(response.text)
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")






#以下類似main
(loginhash,formhash)=get_login_window()  
username = 'Allen_XL_Li'
password = '10708037'
login(loginhash,formhash,username,password)
#print ( loginhash )
#print ( formhash )
