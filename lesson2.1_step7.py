from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    pic_t = browser.find_element_by_id("treasure")
    pic_valuex = pic_t.get_attribute("valuex")
    x = pic_valuex
    y = calc(x)

    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)

    imtherobot = browser.find_element_by_id("robotCheckbox")
    imtherobot.click()
    robotsrule = browser.find_element_by_id("robotsRule")
    robotsrule.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()