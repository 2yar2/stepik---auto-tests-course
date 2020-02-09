from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    iwanttogo = browser.find_element_by_css_selector("button.btn.btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)

    buttonsubmit = browser.find_element_by_css_selector("button.btn.btn-primary").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()