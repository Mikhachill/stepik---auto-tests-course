from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_css_selector('#num1')
    x=int(x.text)
    print("Переменная X",x)
    y=browser.find_element_by_css_selector('#num2')
    y=int(y.text)
    # y.text -достает текст который написан в теге!
    print("Переменная Y", y)
    z=y+x
    print("Переменнеая Z", z)
    z=str(z)

    

    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)
    


    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



