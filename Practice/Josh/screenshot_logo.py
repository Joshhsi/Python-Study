# -*- coding: utf-8 -*-
# 程式 screenshot (Python 3 version)
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select



#針對輸入想查詢的型號關鍵字去各hcl網頁搜尋logo資訊並擷圖
while True:
    Your_Model = str(input("請輸入查詢關鍵字 : "))
    if Your_Model == "" : break
    else:
        # 進入Windows HCL

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        web = webdriver.Chrome(r"D:\code\python\chromedriver.exe", options=options) 
        urlwindows='https://www.windowsservercatalog.com/default.aspx'
        web.maximize_window()
        
        #利用填入欲查詢的型號，開始進入搜尋

        web.get(urlwindows)
        web.find_element_by_name('text').clear()
        web.find_element_by_name('text').send_keys(Your_Model)
        time.sleep(4)
        web.find_element_by_id('searchGo').click()
        web.find_element_by_class_name('productName').click()
        
        osoption = list()
        s1 = Select(web.find_element_by_id('CcitemDetailsdump2_ddlOSFilter'))
        
        #針對有拿認証的版本逐一進去擷圖
        for select in s1.options:
            osoption.append(select.text)

        for select in osoption:
            if select == "(select a compatible Windows version)":
                print('start'+select)
            else:
                print('開始印'+select)
                s2 = Select(web.find_element_by_id('CcitemDetailsdump2_ddlOSFilter'))
                s2.select_by_visible_text(select)
                web.find_element_by_id('submissionByOSGo').click()
                              
                web.execute_script("""
                (
                function () 
                {
                var y = 0;
                var step = 400;
                window.scroll(0, 0);
                    function f() 
                    {
                        if (y < document.body.scrollHeight) 
                        {
                        y  = step;
                        window.scroll(0, y);
                        setTimeout(f, 50);
                    } 
                    else 
                    {
                        window.scroll(0, 0);
                        document.title  = "scroll-done";
                    }
                }
                setTimeout(f, 1000);
                }
                ) 
                ();""")
                    
                time.sleep(2)
                web.save_screenshot("WindowsHCL_"+ Your_Model + '_' + select  + ".png")
        break      
                   
        web.close()









        



