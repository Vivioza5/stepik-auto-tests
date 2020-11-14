from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
link =" http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome('/home/vitaliy/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver')
    browser.get(link)
    time.sleep(1)
    summ=int(browser.find_element_by_css_selector("#num1").text)+int(browser.find_element_by_css_selector("#num2").text)
    print(int(summ))
    browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_tag_name("select"))
    strsumm=str(summ)
    mage=select.select_by_visible_text(strsumm)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


