from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration1.html')

    first_name = browser.find_element_by_css_selector('input.first[required]')
    last_name = browser.find_element_by_css_selector('input.second[required]')
    email = browser.find_element_by_css_selector('input.third[required]')
    first_name.send_keys('Vladimir')
    last_name.send_keys('Golodaev')
    email.send_keys('blabla@blamail.com')

    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(5)

    welcome_txt_elem = browser.find_element_by_tag_name('h1')
    welcome_txt = welcome_txt_elem.text

    assert "Congratulations! You have successfully registered!" == welcome_txt

finally:
    time.sleep(10)
    browser.quit()
