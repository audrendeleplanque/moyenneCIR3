from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from searchMark import searchMark
from calculator import averagePhysics
import time

chrome_options = Options()
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--headless")  # Activer le mode headless
chrome_options.add_argument("--disable-gpu")  # Désactiver l'accélération matérielle
driver = webdriver.Chrome(options=chrome_options)

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

print("Moyenne de physique : ", averagePhysics(transformation, mecaSol, probaStat, analyseDesSignaux, automatique))

driver.close()
