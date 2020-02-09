from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)

    imtherobot = browser.find_element_by_id("robotCheckbox")
    imtherobot.click()


    browser.execute_script("window.scrollBy(0, 100);")

    robot_rule = browser.find_element_by_id("robotsRule").click()
    button_submit = browser.find_element_by_class_name("btn.btn-primary").click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()