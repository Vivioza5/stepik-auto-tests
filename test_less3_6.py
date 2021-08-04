import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('urlid', ["236895","236895","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser,urlid):

    link = f"https://stepik.org/lesson/{urlid}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector(".textarea").send_keys(f"{answer}")
    print(answer)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(5)
    # text_el = WebDriverWait(browser, 10).until(
    #     # EC.visibility_of((By.CLASS_NAME, "smart-hints__hint"))
    #     EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    text_alert = browser.find_element_by_class_name("smart-hints__hint")
    assert text_alert.text=="Correct!"


    # print(text_el)
    # text_alert = browser.find_element_by_css_selector(".smart-hints__hint")

    # assert "Correct!" == text_el.text, "NOT CORRECT!"



    # message=browser.find_element_by_class_name("attemp-message")
    # print(message)
   # browser.find_element_by_css_selector("#login_link")