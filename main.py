from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
print("Scolarité")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/ul/li[2]/a/span').click()
print("Chargement de la page des notes")
time.sleep(10)

note_devops = driver.find_element(By.XPATH, '//*[@id="form:j_idt193_data"]/tr[4]/td[4]/span[2]').text
print("Note de Devops : ",note_devops)
driver.close()