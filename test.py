from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from searchMark import searchMark
import time

driver = webdriver.Chrome()

driver.get("https://aurion.junia.com/faces/Login.xhtml")

# Connexion
driver.find_element(By.ID, "username").send_keys("audren.deleplanque@student.junia.com")
driver.find_element(By.ID, "password").send_keys("cd?32RHb")
driver.find_element(By.ID, "j_idt28").click()
# Fin de la connexion
print("Connected")
driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/a/span[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/ul/li[2]/a/span').click()
print("Chargement de la page des notes")
time.sleep(5)

transformation = searchMark(driver, "2324_ISEN_3A_S1_TRANSFO")
time.sleep(2)
mecaSol = searchMark(driver, "2324_ISEN_CIR3_CNB3_S1_MECASOL")
time.sleep(2)
probaStat = searchMark(driver, "2324_ISEN_3A_S1_PROBA")
time.sleep(2)
analyseDesSignaux = searchMark(driver, "2324_ISEN_3A_S2_ANSIGIM")
time.sleep(2)
automatique = searchMark(driver, "ISEN_3A_S2_AUTO")
time.sleep(2)

print("Transformation : ", transformation)
print("MecaSol : ", mecaSol)
print("ProbaStat : ", probaStat)
print("Analyse des signaux : ", analyseDesSignaux)
print("Automatique : ", automatique)


driver.close()