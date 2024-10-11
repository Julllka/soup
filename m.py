import requests
from pprint import pprint
import bs4
import time

## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

## Ваш код
response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
div_tag = soup.find('div', class_='tm-articles-list')
#pprint(div_tag.text.strip())

#def get_articles(self):
articles_list = soup.findAll('h2', class_='tm-title tm-title_h2')
#pprint(articles_list)

parsed_data = []
for article in articles_list:
    link = article.find('a', class_='tm-title__link')
    #pprint(link['href'])
    link = f"https://habr.com/ru/articles/{article.find('a', class_='tm-title__link')['href']}"
    #pprint(link)

#Получить название статей
response = requests.get('https://habr.com/ru/articles/')
#soup = bs4.BeautifulSoup(response.text, features='lxml')
title = soup.find('h2')
#pprint(title.text.strip())


#время
time = soup.find('time')['datetime']
#pprint (title, time)

parsed_data.append({
    'title': title,
    'link': link,
    'time': time
})
pprint(parsed_data)

if div_tag == KEYWORDS:
    pprint (div_tag(title))
else:
    pprint(None)