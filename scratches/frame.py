import requests
from bs4 import BeautifulSoup


def search_things(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    titulos = []
    body = []
    for titulo in soup.findAll('h5', {'class': 'card-title'}):
        titulos.append(titulo.get_text().strip())

    for bd in soup.findAll('div', {'class': 'card-body'}):
        body.append(bd.get_text().strip())

    posts = {'titulos': titulos, 'body': body}
    return posts


posts = search_things("http://localhost:8888/laravelapp/public/post")
cont = 0
while posts:
    if cont >= 3:
        break
    else:
        print(f"{posts['titulos'][cont]} \n")
        print(posts['body'][cont])
        cont = cont + 1
