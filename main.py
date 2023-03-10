import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_arr(block):  # возвращает массив с текстом элементов block
    arr = []
    for item in block:
        arr += [item.text]
    return arr


def parse(url):
    page = requests.get(url=url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find_all('div', class_="product-price__value")  # получаем элементы с ценами
    title = soup.find_all('div', class_="product-title__head")  # получаем элементы с названиями
    author = soup.find_all('div', class_='product-title__author')  # получаем элементы с авторами
    return [get_arr(price), get_arr(title), get_arr(author)]


if __name__ == '__main__':
    url = 'https://www.chitai-gorod.ru/search?phrase=python&page='
    url_end = '&onlyAvailable=1'
    price_res, title_res, author_res = [], [], []
    for i in range(1, 4):  # заходим на каждую страницу и результаты записываем в один массив
        res = parse(url + str(i) + url_end)
        price_res += res[0]
        title_res += res[1]
        author_res += res[2]
    dict_res = {'Название': title_res, 'Автор': author_res, 'Цена': price_res}
    results = pd.DataFrame.from_dict(dict_res).rename(index=lambda x: x + 1)
    results.to_excel('Python_book.xlsx')  # записываем в excel
