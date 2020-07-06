# 檢查Python的版本
# python --version
#
# 先檢查目前有安裝的module
# pip list
#
# 以下是需要的module，有缺少的module請照以下指令安裝
# python -m pip install selenium  
# python -m pip install urllib3
# python -m pip install BeautifulSoup4
# python -m pip install pandas numpy
# python -m pip install xlwt
# python -m pip install requests
#
import urllib
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np





web2  = requests.get('https://access.redhat.com/ecosystem/hardware/3649241')
soup = BeautifulSoup( web2.text ,'html.parser')
#print (soup)





print ("==========================================================================================")
print ("==========================================================================================")
tableData = soup.find('table',  attrs={'class' :  'table table-cp tablesaw tablesaw-stack' })
#---------------------------table---------------------------
#
#
# --------------------------<thead>------------
#  tr  th th ... th                           -                                        
# --------------------------</thead>-----------
#
#
# --------------------------<tbody>------------ 
#  tr1  th td ... td                          -
#  tr2  th td ... td                          -
#   .   .  .  ...  .                          -
#   .   .  .  ...  .                          -
#   .   .  .  ...  .                          -
#  trX  th td ... td                          -
# ---------------------------</tbody>----------
#
#
#------------------------------------------------------------



rows = list()
columns = list()
r= []
rTotal= []

c = []
th = []
cTotal = []

thead = tableData.find('thead')
# --------------------------<thead>------------ < -----取得thead資料
#   tr  th th ... th                          -
# --------------------------</thead>----------- 






for theadTh in thead.find_all('th') :
    r=  [theadTh.text.replace('\n', '').replace('\xa0', '') ]
    rTotal = rTotal + r

columns = rTotal
#print (columns)



tbody = tableData.find('tbody')
# --------------------------<tbody>------------ < -----只拿body資料      
#  tr1  th td ... td                          -
#  tr2  th td ... td                          -
#   .   .  .  ...  .                          -
#   .   .  .  ...  .                          -
#   .   .  .  ...  .                          -
#  trX  th td ... td                          -
# ---------------------------</tbody>----------



for tbodyTr in tbody.find_all('tr') :
# --------------------------<tbody>------------   
#  tr1  th td ... td                          -  <-----用for迴圈 依序拿出tr，第一個for迴圈拿這個
#  tr2  th td ... td                          -  <-----第二個for迴圈拿這個
#   .   .  .  ...  .                          -  <-----第三個for迴圈拿這個
#   .   .  .  ...  .                          -  <-----
#   .   .  .  ...  .                          -  <-----
#  trX  th td ... td                          -  <-----第X個for迴圈拿這個
#  -------------------------------------------- 



#  --------------------------------------------- 
#   trNum th td td td ... td                     -  <-----下面使2個用for迴圈 分別從tr1,tr2,...trX裡面依序拿出th 跟 td 的資料
#    ^    ^  ^  ^  ^   ^   ^
#  --------------------------------------------- 


    for tbodyTrTh in tbodyTr.find_all('th') :
        tt =  tbodyTrTh.text.replace('\n', '').replace('\xa0', '')
        tt = tt.strip()
        th=  [ tt ] 
        cTotal = cTotal + th




    for tbodyTrTd in tbodyTr.find_all('td') :
        tt2= tbodyTrTd.text.replace('\n', '').replace('\xa0', '')
        tt2 = tt2.strip()
        c=  [tt2] 
        cTotal = cTotal + c


    print (cTotal)
    #print (len(cTotal))
    if (len(cTotal) == 6 ):
        rows.append( cTotal)
    cTotal = []

#print(rows)

df = pd.DataFrame(data=rows, columns=columns)
df.to_excel('table4RHEL.xls')

#print(df)


