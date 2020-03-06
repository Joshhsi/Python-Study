# 安裝 beautifulSoap module 用來抓取網頁的資訊並存入變數裏面，也可以印出來

import time
import urllib.request 
import urllib.error 

from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://zh.wikipedia.org/wiki/Wikipedia%3A%E9%A6%96%E9%A1%B5'

#開啟wiki，調整開啟網頁的大小，再進入歷史上的今天的頁面
web = webdriver.Chrome("/home/alion/Downloads/chromedriver") 
web.get(url)
web.set_window_position(0,0)
web.set_window_size(1920,1080)   
time.sleep(3)
web.find_element_by_link_text('更多歷史事件').click()

# 抓取頁面轉換後的網址
url2 = web.current_url


#用BeautifulSoap抓出頁面的資料
aWebPageData = urllib.request.urlopen(url2) 
soup = BeautifulSoup( aWebPageData ,'html.parser')
#print(soup)


#從soap裏面再抓資訊下來 抓歷史上的今天是那天的資料 （完全不懂怎麼辦到的）
name_box = soup.find('h1', attrs={'class' :  'firstHeading' })
name = name_box.text.strip()
#print(name)


#擷取圖片並加上日期到圖片名字裡
time.sleep(3)
web.save_screenshot("HistoryToday_{}.png".format(name))

# 結束
web.close()
