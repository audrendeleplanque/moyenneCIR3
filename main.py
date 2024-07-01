from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from searchMark import searchMark, searchAdditionalMark
from calculator import averageMaths, averageInfo, averagePhysics
import time

# Récupération des identifiants
username = input("Username: ")
password = input("Password: ")

# Configuration du navigateur
chrome_options = Options()
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--headless")  # Activer le mode headless
chrome_options.add_argument("--disable-gpu")  # Désactiver l'accélération matérielle
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://aurion.junia.com/faces/Login.xhtml")

# Connexion
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "j_idt28").click()
# Fin de la connexion
try:
    driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/a/span[2]').click()
    print("Connected")
except:
    print("Error: Wrong email or password")
    driver.close()
    exit()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="form:sidebar"]/div/div[2]/ul/li[3]/ul/li[2]/a/span').click()
print("Loading marks page")
time.sleep(5)

# Calcul de la moyenne de physique
mecaQ = searchMark(driver, "MECAQ")
elecNum = searchMark(driver, "numérique")
elecNum = searchAdditionalMark(driver, "TP Microcontroleurs", elecNum)
print(elecNum)
projetElec = searchMark(driver, "Projet d'électronique")
physiqueSol = searchMark(driver, "Physique du solide")
ElecAna = searchMark(driver, "ElecAna")

print("Moyenne de physique : ", averagePhysics(mecaQ, elecNum, projetElec, physiqueSol, ElecAna))

"""
# Calcul de la moyenne de mathématique
transformation = searchMark(driver, "2324_ISEN_3A_S1_TRANSFO")
mecaSol = searchMark(driver, "2324_ISEN_CIR3_CNB3_S1_MECASOL")
probaStat = searchMark(driver, "2324_ISEN_3A_S1_PROBA")
analyseDesSignaux = searchMark(driver, "2324_ISEN_3A_S2_ANSIGIM")
automatique = searchMark(driver, "ISEN_3A_S2_AUTO")
print("Moyenne de mathématique : ", averageMaths(transformation, mecaSol, probaStat, analyseDesSignaux, automatique))

# Calcul de la moyenne d'informatique
java = searchMark(driver, "2324_ISEN_CIR3_S1_JAVA")
infographie = searchMark(driver, "2324_ISEN_CIR3_S1_INFOGRAPHIE")
projetInfo = searchMark(driver, "2324_ISEN_CIR3_S1_PROJET_INFO")
BDD = searchMark(driver, "BDD")
reseau = searchMark(driver, "2324_ISEN_3A_S2_RSX")
devops = searchMark(driver, "2324_ISEN_CIR3_S2_DEVOPS")
print("Moyenne d'informatique : ", averageInfo(java, infographie, projetInfo, BDD, reseau, devops))

"""

driver.close()
