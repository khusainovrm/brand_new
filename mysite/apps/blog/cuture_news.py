from bs4 import BeautifulSoup
import requests


def culture():
    final_news = []
    url = requests.get ('https://www.culture.ru/news/')

    soup = BeautifulSoup(url.text, features="html.parser")
    raw_news = soup.find_all('a', {'class': 'card-heading_title-link'})

    #Создание списка в человеческом виде
    for i in range(len(raw_news)):
        final_news.append((raw_news[i].text, "https://www.culture.ru" + raw_news[i].get ('href')))
    return final_news
