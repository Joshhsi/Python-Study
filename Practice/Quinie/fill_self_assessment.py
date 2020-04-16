# 緯創防疫自我檢視填寫提醒
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import Select

# 進入緯創防疫自我檢視網頁
web = webdriver.Chrome("D:\python\chromedriver.exe") 
urlwindows='https://familyweb.wistron.com/whrs/login.aspx'
web.get(urlwindows)
#視窗最大化，方便畫面易讀
web.maximize_window()

#清空欄位&填入mail英文名稱
web.find_element_by_name('username').clear()
web.find_element_by_name('username').send_keys('quinie_chen')
#清空欄位&填入工號
web.find_element_by_name('userpass').clear()
web.find_element_by_name('userpass').send_keys('10112008')
#按下登入(使用xpath識別按鍵)
#web.find_element_by_partial_link_text('登入').click()
web.find_element_by_xpath('//*[@id="loginform"]/form/div/input[3]').click()
#執行下一步動前，稍等四秒，等待確認登入後執行下步動作
time.sleep(4)
#popup 確認視窗，提醒回填防疫相關資訊
web.execute_script("window.alert('請填寫緯創防疫自我檢視填報網站');")    

#isChecked = web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[15]')
#web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[20]').click()
#isChecked = web.findElement(By.xpath('//*[@id="loginform"]/div/form/input[15]'));
# if web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[16]').is_selected():
#     print ('selected!')
# else:
#     print('選擇的內容是name：')
#     print(web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[16]').get_attribute('value'))
#     checked_value = web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[16]').get_attribute('value')
#     if (checked_value == '1'):
#         web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[16]').click()
#         web.find_element_by_xpath('//*[@id="loginform"]/div/form/input[21]').click()
#         dialog_box = web.switch_to_alert()
#         '''新增等待時間'''
#         time.sleep(2)
#         '''獲取對話方塊的內容'''
#         #列印警告對話方塊內容
#         print (dialog_box.text)  
#         '''點選【確認】顯示"您為何如此自信？"'''
#         dialog_box.accept()   #接受彈窗
#     else:  print('選擇的內容不是1，取消!')   

#web.close()



        



