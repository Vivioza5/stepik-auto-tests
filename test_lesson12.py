import time
from pathDriver import path_driver
import pytest
from selenium import webdriver
# не забываем оставить пустую строку в конце файла
link = "http://suninjuly.github.io/registration1.html"
link1 = "http://suninjuly.github.io/registration2.html"
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def action_on_page(browser):
     browser.get(link)
     input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
     input1.send_keys("Ivan")
     input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
     input2.send_keys("Petrov")
     input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
     input3.send_keys("Petrov@gmail.com")
     input4 = browser.find_element_by_css_selector("div.second_block input.form-control.first")
     input4.send_keys("0986134770")
     input5 = browser.find_element_by_css_selector("div.second_block input.form-control.second")
     input5.send_keys("Smolensk")
     button = browser.find_element_by_css_selector("button.btn")
     button.click()
     time.sleep(1)
     welcome_text_elt = browser.find_element_by_tag_name("h1")
     welcome_text = welcome_text_elt.text
     time.sleep(10)
     return welcome_text
@pytest.fixture()
def action_on_page1(browser):
     browser.get(link1)
     input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
     input1.send_keys("Ivan")
     input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
     input2.send_keys("Petrov")
     input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
     input3.send_keys("Petrov@gmail.com")
     input4 = browser.find_element_by_css_selector("div.second_block input.form-control.first")
     input4.send_keys("0986134770")
     input5 = browser.find_element_by_css_selector("div.second_block input.form-control.second")
     input5.send_keys("Smolensk")
     button = browser.find_element_by_css_selector("button.btn")
     button.click()
     time.sleep(1)
     welcome_text_elt = browser.find_element_by_tag_name("h1")
     welcome_text = welcome_text_elt.text
     time.sleep(10)
     return welcome_text

class TestAbs():
    def test_blue(self,action_on_page):
        # page=action_on_page(link)
        msg="Congratulations! You have successfully registered!"
        assert action_on_page==msg
    def test_blue1(self,action_on_page1):
        # page=action_on_page(link)
        msg="Congratulations! You have successfully registered!"
        assert action_on_page1==msg

     # return welcome_text

    # def test_welcome_text(self,welcome_text):
    #     #  page1 = action_on_page(link1)
    #     # self.assertEqual(page1, "Congratulations! You have successfully registered!", "not registered")
    #     msg="Congratulations! You have successfully registered!"
    #     assert welcome_text==msg, "Congratulations! You have successfully registered!" "not registered"










