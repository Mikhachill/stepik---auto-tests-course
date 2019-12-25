from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os



try:
    browser = webdriver.Chrome()
    #говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button1=browser.find_element_by_id('book')
    button1.click()

    x=browser.find_element_by_css_selector('.nowrap#input_value')
    x=int(x.text)
    y=str(math.log(abs(12*math.sin(x))))
    
    input1=browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button2=browser.find_element_by_css_selector('button[id="solve"]')
    button2.click()

                                    

                        
                                        

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()





