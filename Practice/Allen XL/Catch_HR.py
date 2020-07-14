import time
from selenium import webdriver
from getpass import getpass


# selenium
# 安全連線的排除
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


# selenium
# 開啟瀏覽器並前往網址頁面
web = webdriver.Chrome("D:\chromedriver.exe", options=options) 
urlwindows='https://hr.wistron.com/psp/PRD/EMPLOYEE/HRMS/?cmd=logout'
web.get(urlwindows)


# time
# 暫停4秒
time.sleep(4)


# selenium
# 清空欄位&填入mail英文名稱
web.find_element_by_name('userid').clear()
web.find_element_by_name('userid').send_keys('10708037')


# selenium
# 清空欄位&填入工號
web.find_element_by_name('pwd').clear()
#web.find_element_by_name('pwd').send_keys('xxx')
web.find_element_by_name('pwd').send_keys(getpass())
web.find_element_by_name('Submit').click()
time.sleep(4)



# selenium
# 出勤紀錄xpath: //*[@id="ADMN_WIS_ESS_SERV_REQUEST_HMPG_Data"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/a
web.find_element_by_xpath('//*[@id="ADMN_WIS_ESS_SERV_REQUEST_HMPG_Data"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/a').click()

