import unittest
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
link1 = "http://suninjuly.github.io/registration2.html"


def action_on_page(link):
    browser.get(link)
    input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    input3.send_keys("Petrov@gmail.com")
    # input3 = browser.find_element_by_class_name("form-control.city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    return welcome_text


try:
    browser = webdriver.Chrome()
    page1 = action_on_page(link)
    page2 = action_on_page(link1)
    print(page1)

#     # browser.get("http://suninjuly.github.io/registration1.html")
#     # input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
#     # input1.send_keys("Ivan")
#     # input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
#     # input2.send_keys("Petrov")
#     # input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
#     # input3.send_keys("Petrov@gmail.com")
#     # # input3 = browser.find_element_by_class_name("form-control.city")
#     # # input3.send_keys("Smolensk")
#     # # input4 = browser.find_element_by_id("country")
#     # # input4.send_keys("Russia")
#     # button = browser.find_element_by_css_selector("button.btn")
#     # button.click()
#     # time.sleep(1)
#     # welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # welcome_text = welcome_text_elt.text
#     #
#     # print(welcome_text)
#     # assert "Congratulations! You have successfully registered!" == welcome_text
finally:
# успеваем скопировать код за 30 секунд
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла
class TestAbs(unittest.TestCase):
    def test_welcome_text(self):
        self.assertEqual("Congratulations! You have successfully registered!", page1,
                         "Should be absolute value of a number")

    # def test_abs2(self):
    #     self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
    TestAbs.test_welcome_text(page1)
    TestAbs.test_welcome_text(page2)
