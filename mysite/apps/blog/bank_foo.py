from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.banki.ru/products/currency/cash/moskva/')
data = response.text
#print(data)
def bank():
    all_bank =[]
    bank_list = []
    currency_all=[]
    currnecy_list = []

    soup = BeautifulSoup(data, features="html.parser")
    all_bank = soup.find_all('a', {'data-test' : "bank-name"})

    #Создание списка в человеческом виде
    for i in range(len(all_bank)):
        bank_list.append(all_bank[i].text)
    return bank_list


def currency():
    currency_all = []
    currnecy_list = []

    soup = BeautifulSoup (data, features="html.parser")
    currency_all = soup.find_all ('div', {'class': "table-flex__cell table-flex__rate font-size-large"})

    # Создание списка в человеческом виде
    for i in range (len (currency_all)):
        currnecy_list.append (currency_all[i].text)
    return currnecy_list

print(currency)