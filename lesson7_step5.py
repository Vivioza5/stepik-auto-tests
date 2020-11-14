from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome('/home/vitaliy/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver')
    browser.get(link)
    x_element= browser.find_element_by_css_selector("#input_value")
    y=calc(x_element.text)
    input1=browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    option1= browser.find_element_by_css_selector("[for=robotCheckbox]")
    option1.click()
    option2= browser.find_element_by_css_selector("[for=robotsRule]")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

