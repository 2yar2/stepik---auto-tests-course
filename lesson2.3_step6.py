﻿from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    flybutton = browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)    

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