import time
import requests
import urllib
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup




# requests
# BeautifulSoup
# 把ubuntu官網的Table用request抓下來，再透過BeautifulSoup轉成html網頁碼
web  = requests.get('https://wiki.ubuntu.com/Releases')
soup = BeautifulSoup( web.text ,'html.parser')
table = soup.find_all('table')[1]
print(table)  



# urllib(內建)
# urllib也可以抓table
# html = urllib.request.urlopen("https://wiki.ubuntu.com/Releases").read()
# soup = BeautifulSoup(html, 'html.parser')
# table = soup.find_all('table')[1]




# 建立list，一個存table第一列的資料，一個存剩下每列的資料
columns = list() 
rows = list()
rowTotal = list()


# 抓出table的第一列 
tr0 = table.find_all('tr')[0]                                    # 抓第一個tr的資料出來
for td in tr0.find_all('td') :                                   # 找這個tr裡面所有的td
    c =  [td.text.replace('\n', '').replace('\xa0', '') ]        # 把td資料轉為純文字
    columns = columns + c                                        # 一個一個收集到columns list裡面
print(columns)



# 抓出table剩下每一列
trs = table.find_all('tr')[1:]                                   # 抓剩下的每一個tr
for trR in trs:                                                  # 用迴圈一個一個看tr內的資料
    for td in trR.find_all('td') :                               # 找一個tr裡面所有的td
        r =  [ td.text.replace('\n', '').replace('\xa0', '') ]   # 把td資料轉為純文字
        rowTotal = rowTotal + r                                  # 收集到rowTotal list裡面
    rows.append(rowTotal)                                        # rows list 中加入 rowTotal作為一列tr所收集到的資訊
    rowTotal = []                                                # 清空rowsTotal 開始下一個tr的處理
print(rows)


# pandas 
# 使用pandas裡面的DataFrame 把剛收集的兩個資料存成表格
# 最後匯出excel
df = pd.DataFrame(data=rows, columns=columns)
df.to_excel('UbuntuSchedule.xls')
#print(df.head()) # just print the fisrt 5 rows  
print(df)
