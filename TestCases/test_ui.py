from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest

url = "http://localhost:4000/ui"
driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(30)


def setup():
    # print("setup")
    pass


def teardown_module(module):
    driver.close()


def test_add_sub():
    # Проверка на добавление подписки
    driver.get("http://localhost:4000/ui")
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("test1@mail.ru")
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys("test1")
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    time.sleep(1)
    name = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/th").text
    assert "test1" == name
    email = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]").text
    assert "test1@mail.ru" == email


def test_count_record_less_five():
    # Проверка, что элементов на странице <= 5
    driver.get("http://localhost:4000/ui")
    record_count = len(driver.find_elements_by_xpath("/html/body/div/div/div[2]/div[3]/div/div/table/tbody/tr[*]"))
    assert record_count <= 6


def test_wrong_email():
    # Неправильное заполнение email
    driver.get("http://localhost:4000/ui")
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("wrong_email")
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys("test1")
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    time.sleep(1)
    email = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]").text
    assert "wrong_email" != email


def test_clear():
    # Проверка работы очистки 
    driver.get("http://localhost:4000/ui")
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    time.sleep(1)
    record_count = len(driver.find_elements_by_xpath("/html/body/div/div/div[2]/div[3]/div/div/table/tbody/tr[*]"))
    assert record_count == 1


"""test_add_sub()
test_count_record_less_five()
test_wrong_email()
test_clear()"""
