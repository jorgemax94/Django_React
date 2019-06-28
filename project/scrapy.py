#importe a biblioteca usada para consultar uma URL
from urllib.request import Request, urlopen

##importando panda para dataset
import pandas as pd

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#importando Json
import json as json


def scrapy():
    #varáveis para armazenamento do scraping
    name = []
    link = []
    price = []

    test_json = {}

    #especificando a URL
    req  = Request('https://nerdstore.com.br/categoria/especiais/game-of-thrones/', headers={'User-Agent': 'Mozilla/5.0'})

    #Consulte o site e retorne o html para a variável 'page'
    page = urlopen(req).read()

    #Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    #Pegar valor no HTML
    list_products = soup.find_all('li', class_='product')

    ##Adicionando os valores recuperados a variável
    for products in list_products:
        name.append(products.a.find('h2').text)
        price.append(products.a.find('span', class_ = 'woocommerce-Price-amount amount').text)
        link.append(products.a.find('img')['src'])
        test_json = {
            "name": name,
            "linkImage": link,
            "price": price
        }

    test_json = json.dumps(test_json)

    test_df = pd.DataFrame({
        'name': name,
        'linkImage': link,
        'price': price
    })
    test_df


    #mostrando valores
    print(len(products)) # todos
    print('##############JSON###############')
    print(test_json)
    print('##################PANDA###########')
    print(test_df)
    return test_json
