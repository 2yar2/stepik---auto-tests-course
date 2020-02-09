from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    firstname1 = browser.find_element_by_name("firstname")
    firstname1.send_keys("1")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("2")
    email = browser.find_element_by_name("email")
    email.send_keys("mail@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'find_element.txt')
    print(os.path.abspath(os.path.dirname(__file__)))
    element1 = browser.find_element_by_id("file")
    element1.send_keys(file_path)

    submit1 = browser.find_element_by_css_selector("button.btn.btn-primary").click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()