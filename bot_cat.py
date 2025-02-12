import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

#Definicio URL orginen
url = "https://administraciopublica.gencat.cat/ca/treballar-a-la-generalitat/ofertes-de-treball-temporal/"

#Comprovar connexió
status = requests.get(url).status_code

if status == 200:
    print("Connexió correcta: codi %i" %status)
else:
    print("Connexió no establerta: codi %i" %status)    

#Temps d'espera
def temps_espera():
    t_espera = random.uniform(0.5, 2)
    time.sleep(t_espera)

#Càrrega navegador. Configuració opcions navegació
navegador = webdriver.Firefox()

navegador.get(url)

temps_espera()

#Tractament missatge cookies
cookies = navegador.find_element(by = By.ID, value='ppms_cm_reject-all')

cookies.click()

#Webcrawler

#C1 - Ofertes de treball de caràcter temporal dels departaments de l'Administració de la Generalitat
#c1 = navegador.find_element(by=By.CSS_SELECTOR, value='a.collapsed')

#actions = ActionChains(navegador)
#actions.move_to_element(c1).click().perform()

temps_espera()

#Selecció enllaços i departaments

soup = BeautifulSoup(navegador.page_source, 'html.parser')
departaments = soup.find_all('span', class_='list-group-item-wrapper-content')

dep = []

for d in departaments:
    #print(d.get_text())
    dep.append(d.get_text())

print(dep[1:17])

#Crear funcio Diff per comparar informació fitxers


#Guardar dades en fitxer




## afegir temps aleatori per navegació
## aconseguir columnes de data extracció, nom departament, url feina
## data eliminació, 

#navegador.quit()