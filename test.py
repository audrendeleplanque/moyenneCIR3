from selenium import webdriver
from selenium.webdriver.common.by import By
from searchMark import searchMark
from calculator import averageMaths, averageInfo
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
print("Loading marks page")
time.sleep(5)



transformation = searchMark(driver, "2324_ISEN_3A_S1_TRANSFO")
mecaSol = searchMark(driver, "2324_ISEN_CIR3_CNB3_S1_MECASOL")
probaStat = searchMark(driver, "2324_ISEN_3A_S1_PROBA")
analyseDesSignaux = searchMark(driver, "2324_ISEN_3A_S2_ANSIGIM")
automatique = searchMark(driver, "ISEN_3A_S2_AUTO")

print("Moyenne de mathématique : ", averageMaths(transformation, mecaSol, probaStat, analyseDesSignaux, automatique))

java = searchMark(driver, "2324_ISEN_CIR3_S1_JAVA")
infographie = searchMark(driver, "2324_ISEN_CIR3_S1_INFOGRAPHIE")
projetInfo = searchMark(driver, "2324_ISEN_CIR3_S1_PROJET_INFO")
BDD = searchMark(driver, "BDD")
print("BDD : ", BDD)
reseau = searchMark(driver, "2324_ISEN_3A_S2_RSX")
devops = searchMark(driver, "2324_ISEN_CIR3_S2_DEVOPS")

print("Moyenne d'informatique : ", averageInfo(java, infographie, projetInfo, BDD, reseau, devops))

driver.close()