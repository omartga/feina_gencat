import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#Definicio URL orginen
url = "https://administraciopublica.gencat.cat/ca/treballar-a-la-generalitat/ofertes-de-treball-temporal/"

#Comprovar connexió
resposta_web = requests.get(url)
print(resposta_web.status_code)

soup = BeautifulSoup(resposta_web.content, 'lxml')
print(soup.prettify())

print(soup.title.string)
#Càrrega navegador. Configuració opcions navegació



#Webcrawler




#Crear funcio Diff per comparar informació fitxers


#Guardar dades en fitxer




## afegir temps aleatori per navegació
## aconseguir columnes de data extracció, nom departament, url feina
## data eliminació, 
    
