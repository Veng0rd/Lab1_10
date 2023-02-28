import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_arr(block):  # возвращает массив с текстом элементов в block
    arr = []
    for item in block:
        arr += [item.text]
    return arr


def parse():
    url = 'https://www.chitai-gorod.ru/search?q=Python&page=1'
    page = requests.get(url=url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find_all('div', class_="product-price__value")  # получаем элементы с ценами
    title = soup.find_all('div', class_="product-title__head")  # получаем элементы с названиями
    author = soup.find_all('div', class_='product-title__author')  # получаем элементы с авторами
    results = pd.DataFrame({'Название': get_arr(title), 'Автор': get_arr(author), 'Цена': get_arr(price)}).rename(
        index=lambda x: x + 1)
    results.to_excel('Python_book.xlsx')


if __name__ == '__main__':
    parse()
