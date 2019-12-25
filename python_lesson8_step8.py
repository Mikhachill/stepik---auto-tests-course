from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

with open("test.txt", "w") as file:
    content = file.write("1")


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1=browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys('Mi')

    input2=browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys('Mik')

    input3=browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys('Mikh')

    current_dir = os.path.abspath(os.path.dirname(__file__))   
          # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')    
          # добавляем к этому пути имя файла
    element=browser.find_element_by_css_selector('[type="file"]')
    element.send_keys(file_path)


    button = browser.find_element_by_tag_name("button")
    button.click()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    



