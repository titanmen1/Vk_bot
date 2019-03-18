import requests
from lxml import html



def pars():
    #url = 'https://rjite.ru/citata-pacanskie'
    #response = requests.get(url)

    # Преобразование тела документа в дерево элементов (DOM)
    #parsed_body = html.fromstring(response.text)

    # Выполнение xpath в дереве элементов
    # print(parsed_body.xpath('//title/text()')) # Получить title страницы
    # print(parsed_body.xpath('//p/text()')) # Получить аттрибут href для всех ссылок

    #pars = parsed_body.xpath('//p/text()')
    #print(len(pars))

    f = open('text.txt', 'r', encoding='UTF-8')
    pars = f.read().split(' | ')
    f.close()
    return pars

