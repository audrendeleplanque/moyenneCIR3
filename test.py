from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
print("Scolarité")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/ul/li[2]/a/span').click()
print("Chargement de la page des notes")
time.sleep(10)

note_devops = driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div[3]/div[4]/div/div[3]/div[2]/table/tbody/tr[4]/td[4]/span[2]').text
print("Note de Devops : ",note_devops)
driver.close()