from bs4 import BeautifulSoup
import requests as req


class NextPage:
    def __init__(self, link):
        self.link = link
        self.i = 1

    def __next__(self):
        resp = req.get(self.link + '/' + f'{self.i}')
        if resp.status_code == 200:
            print(f'Страница {self.i}.')
            self.i += 1
            return resp
        else:
            print('Все станицы записаны.')
            raise StopIteration

    def __iter__(self):
        return self


def write(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    a = soup.select_one('p')
    a.decompose()
    tags = soup.find_all('p')
    for tag in tags:
        with open(f'{soup.title.text.split(" читать онлайн")[0]}.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.write(" ".join(tag.text.split() + ['\n']))


all_pages = NextPage('https://knizhnik.org/dzheffri-diver/dvenadczataja-karta')
for page in all_pages:
    write(page)
