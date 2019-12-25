from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)

    x=browser.find_element_by_css_selector('.nowrap#input_value')
    x=int(x.text)
    y=str(math.log(abs(12*math.sin(x))))
    
    input1=browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button1=browser.find_element_by_tag_name("button")
    button1.click()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()





