import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import string
import keyboard
import pyttsx3

dolarantigo = 0

while True:

    time.sleep(1)

    url = 'https://economia.uol.com.br/cotacoes/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = str(soup.findAll("a","subtituloGrafico subtituloGraficoValor"))

    contentstr = str(content)
    numbers = ''
    for word in contentstr.split('>'):
        if word.startswith('R$'):
            numbers += word

    i = 0
    dolar = ''
    while i <= 6:
        dolar += numbers[i]
        i += 1

    print(dolar)

    if dolar != dolarantigo:
        engine = pyttsx3.init()
        engine.say('o dólar está valendo ' + dolar)
        engine.runAndWait()
        dolarantigo = dolar
        
    if keyboard.is_pressed('esc'):
        break

