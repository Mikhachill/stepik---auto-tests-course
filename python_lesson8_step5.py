from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time




try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



