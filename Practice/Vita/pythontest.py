from selenium import webdriver
#使用chrome的webdriver
browser = webdriver.Chrome()
#開啟google首頁
browser.get('https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe')
#如果需要執行完自動關閉，就要加上下面這一行
#browser.close()
#https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
