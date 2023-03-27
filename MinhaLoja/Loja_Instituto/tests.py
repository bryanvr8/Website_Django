from django.test import TestCase
import requests

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
cotacao = cotacao.json()
cotacao_dolar = cotacao['USDBRL']['bid']

print(cotacao_dolar)
    


# Create your tests here.
