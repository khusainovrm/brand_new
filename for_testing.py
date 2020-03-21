from bs4 import BeautifulSoup
import requests

url = 'https://www.culture.ru/news/'
page = requests.get (url)
soup = BeautifulSoup (page.text, "html.parser")

final_news = []
news = []

news = soup.findAll ('a', {'class': 'card-heading_title-link'})
for n in news:
    news_title = n.text
    news_url = ("https://www.culture.ru" + n.get('href'))
    final_news.append ((news_title, news_url))

print(final_news)

# <div class="table-flex__cell table-flex__rate font-size-large text-nowrap" data-currencies-code="EUR" data-currencies-rate-sell="87.1">
# <a class="card-heading_title-link" href="/news/255540/programma-detskii-weekend-festivalya-zolotaya-maska-otkrylas-v-moskve">Программа «Детский Weekend» фестиваля «Золотая маска» открылась в Москве</a>
