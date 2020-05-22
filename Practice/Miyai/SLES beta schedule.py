# 緯創防疫自我檢視填寫提醒
from datetime import date
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import Select

# 進入緯創防疫自我檢視網頁
web = webdriver.Chrome("D:\python\chromedriver.exe") 
urlwindows='https://suse.com/betaprogram/sle-beta/#releases'
web.get(urlwindows)
#視窗最大化，方便畫面易讀

today=date.today()

web.save_screenshot("SLES schedule_{}.png".format(today))
time.sleep(3)

web.close()

        



