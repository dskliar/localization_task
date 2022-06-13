from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_present(browser):
    browser.get(link)
    assert WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add_to_basket_form']/button"))), "Add button is not found"
    