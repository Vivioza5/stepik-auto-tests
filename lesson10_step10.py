
from selenium import webdriver
import time
import math

link ="http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome('/home/vitaliy/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver')
    browser.get(link)
    x_element= browser.find_element_by_css_selector("#input_value")
    y=calc(x_element.text)
    input1=browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    option1= browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2=browser.find_element_by_css_selector("[for=robotsRule]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    print(x_element.text)
    time.sleep(1)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


