from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math




try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x=browser.find_element_by_css_selector('.nowrap#input_value')
    x=int(x.text)
    y=str(math.log(abs(12*math.sin(x))))

    

    
    input1=browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option2 = browser.find_element_by_css_selector('#robotsRule')
    option2.click()

    
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    



