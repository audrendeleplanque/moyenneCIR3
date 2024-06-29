from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def searchMark(driver, subject):
    dict = {}
    markPresence = True
    i = "1"
    driver.find_element(By.ID, "form:search-texte").send_keys(subject)
    driver.find_element(By.ID, "form:search").click()
    time.sleep(5)

    while markPresence:
        try:
            title = driver.find_element(By.XPATH, '//*[@id="form:j_idt193_data"]/tr['+i+']/td[3]/span[2]').text
            mark = driver.find_element(By.XPATH, '//*[@id="form:j_idt193_data"]/tr['+i+']/td[4]/span[2]').text
            dict[title] = mark
            i = str(int(i) + 1)
        except:
            markPresence = False
            break

    return dict