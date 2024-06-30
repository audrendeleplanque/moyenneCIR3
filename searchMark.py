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
    driver.find_element(By.ID, "form:search-texte").send_keys(Keys.CONTROL, 'a')
    driver.find_element(By.ID, "form:search-texte").send_keys(Keys.DELETE)

    while markPresence:
        try:
            title = driver.find_element(By.XPATH, '//*[@id="form:j_idt193_data"]/tr[' + i + ']/td[3]/span[2]').text
            mark = driver.find_element(By.XPATH, '//*[@id="form:j_idt193_data"]/tr[' + i + ']/td[4]/span[2]').text
            dict[title] = mark
            i = str(int(i) + 1)
        except:
            markPresence = False
            break

        # Vérifier la présence de "2nde session" ou "session" dans les clés
        if any("2nde session" in key or "session" in key for key in dict):
            # Liste des clés à supprimer
            cles_a_supprimer = [cle for cle in dict if "Partiel" in cle]

            # Supprimer les clés identifiées
            for cle in cles_a_supprimer:
                del dict[cle]

    return dict
