from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1")
    x = number1.text
    number2 = browser.find_element_by_id("num2")
    y = number2.text


    def calc(x,y):
      return str(int(x)+int(y))

    
    element1 = browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("[value='" + calc(x,y) + "']").click()
    element1 = browser.find_element_by_id("dropdown").click()

    button = browser.find_element_by_css_selector("button.btn.btn-default").click()

    time.sleep(10)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()