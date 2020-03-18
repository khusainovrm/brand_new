from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.banki.ru/products/currency/cash/moskva/')
data = response.text

soup = BeautifulSoup(data, features="html.parser")
currency_all = soup.find_all('div', {'data-currencies-code':'EUR'})
result = soup.find_all(lambda tag: tag.name == 'div' and
                                   tag.get('data-currencies-code') == ['EUR'])

currency_all = []
currency_list = []


print(currency_all)

# Создание списка в нормальном виде
for i in range(len(currency_all)):
    currency_list.append(currency_all[i].text)

print(currency_list)

#<div class="table-flex__cell table-flex__rate font-size-large   text-nowrap" data-currencies-rate-sell="83.78" data-currencies-code="EUR">
#83,78
#<i class="icon-font icon-calculator-16 icon-font--size_small calculator-hover-icon" data-click="open-converter"></i>


"""data-currencies-rate-buy="81.8" data-currencies-code="EUR">
													81,80
<i class="icon-font icon-calculator-16 icon-font--size_small calculator-hover-icon" data-click="open-converter"></i>
</div>
<div class="table-flex__cell table-flex__rate font-size-large   text-nowrap"
data-currencies-rate-sell="83.1" data-currencies-code="EUR">
83,10
<i class="icon-font icon-calculator-16 icon-font--size_small calculator-hover-icon" data-click="open-converter"></i>"""