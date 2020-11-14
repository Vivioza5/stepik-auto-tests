from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome('/home/vitaliy/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver')
    browser.get(link)
    x_element= browser.find_element_by_css_selector("#treasure")
    people_checked = int(x_element.get_attribute("valuex"))
    y=calc(people_checked)
    input1=browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    option1= browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2= browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    print(people_checked)







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
