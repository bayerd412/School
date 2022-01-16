from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from rich.console import Console
import json
from requests.exceptions import MissingSchema, InvalidSchema

items = [
    "http://gymnaz1-murm.ru/",
    "http://2gimn51.ru/",
    "http://gym3murmansk.ucoz.ru/",
    "http://gimn5.murm.eduru.ru/news",
    "http://gymn6.com.ru/",
    "http://gim7.murm.eduru.ru/",
    "http://www.gimnazia8.ru/",
    "https://mml.ucoz.org/",
    "http://www.mplmurmansk.ru/",
    "http://murmanprg24.ucoz.ru/",
    "http://prog40.ru/novosti",
    "https://progimnaziya.murm.eduru.ru/news",
    "http://progimnaziya61.murm.eduru.ru/news",
    "http://mschool1.ru/",
    "http://roslshk.moy.su/",
    "https://murm-shkola4.murm.eduru.ru/news",
    "http://mou-school11.ucoz.ru/",
    "http://www.mou16-murmansk.ru/",
    "http://my-school18.ucoz.ru/",
    "http://kadet-murmansk.ru/news/",
    "http://www.school20.com.ru/index.php/novosti-i-ob-yavleniya",
    "https://school21.murm.eduru.ru/news",
    "http://www.school22mur.ru/",
    "http://school23mur.ucoz.ru/",
    "http://school27-murman.my1.ru/index/novosti_i_objavlenija/0-136",
    "http://skosh8.ucoz.ru/",
    "http://school28.ucoz.ru/",
    "https://skole31.murm.eduru.ru/news",
    "http://murman-school33.ucoz.ru/",
    "https://school34-murman.my1.ru/",
    "http://school36.murmansk.su/",
    "http://www.school42.znaet.ru/",
    "http://sc43murm.com.ru/index.php/novosti",
    "http://murman-school44.ru/",
    "https://sosh45.murm.eduru.ru/news",
    "https://school49.murm.eduru.ru/news",
    "http://school50.su/",
    "http://murmansk57.ru/",
    "http://www.school58.org.ru/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

find_links = []

info = []
console = Console()

searching_text = []
searching_text_1 = input('Введите первое ключевое слово или словосочетание для поиска: ')
searching_text_2 = input('Введите второе ключевое слово или словосочетание для поиска: ')
searching_text_3 = input('Введите первое ключевое слово или словосочетание для поиска: ')
searching_text_4 = input('Введите первое ключевое слово или словосочетание для поиска: ')
searching_text_5 = input('Введите первое ключевое слово или словосочетание для поиска: ')
searching_text_6 = input('Введите первое ключевое слово или словосочетание для поиска: ')

searching_text.extend([searching_text_1, searching_text_2, searching_text_3, searching_text_4, searching_text_5, searching_text_6])
    

def parse_with_links():
    
    count = 0
    while count != 6:
        
        for item in items:
            url = item
            
            req = requests.get(url, headers=headers, allow_redirects=False)
            src = req.text
            
            soup = BeautifulSoup(src, 'lxml')
                    
            find_text = soup.find_all(text=re.compile(searching_text[count])) 
            
            if find_text != []:
                items.remove(url)
                info.append(url)
                find_links.append(url)
            else:
                links = soup.find_all('a')
                
                for link in links:
                    
                    try:
                    
                        req = requests.get(link.get('href'))
                        src = req.text
                        
                        soup = BeautifulSoup(src, 'lxml')
                        
                        find_text = soup.find_all(text=re.compile(searching_text[count]))
                        if find_text != []:
                            if str(link.get('href')) == 'https://www.gosuslugi.ru/342164/2' or 'https://www.gosuslugi.ru' or 'https://www.youtube.com/' or 'https://maps.yandex.ru/-/CVwZMQ7Q':                           
                                pass
                            else:
                                find_links.append(link.get('href'))
                                items.remove(url)
                                info.append(url)
                                break
                    except Exception:
                        pass
                        
                    
        with open(f'{searching_text_1}_найдено.json', 'w', encoding='utf_8_sig') as file:
            json.dump(info, file, ensure_ascii=False, indent=4)
                
        with open(f'{searching_text_1}_не_найдено.json', 'w', encoding='utf_8_sig') as file:
            json.dump(items, file, ensure_ascii=False, indent=4)
            
        with open(f'{searching_text_1}_ссылки.json', 'w', encoding='utf_8_sig') as file:
            json.dump(find_links, file, ensure_ascii=False, indent=4)    
            
        print(searching_text[count])
            
        count += 1 
    
    for i in items:
        console.print(f'{i} -- [red]текст не обнаружен[/red]')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    for i in info:
        console.print(f'{i} -- [green]текст обнаружен[/green]')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')  
    for i in find_links:
        console.print(f'[green]{i}[/green]')      
    

def parse():

    count = 0
    while count != 6:

        for item in items:
            url = item
            
            req = requests.get(url, headers=headers, allow_redirects=False)
            src = req.text
            
            soup = BeautifulSoup(src, 'lxml')
                    
            find_text = soup.find_all(text=re.compile(searching_text[count])) 
            
            if find_text != []:
                items.remove(url)
                info.append(url)
                find_links.append(url)
            else:
                pass
                    
                                                
        with open(f'{searching_text_1}_найдено.json', 'w', encoding='utf_8_sig') as file:
            json.dump(info, file, ensure_ascii=False, indent=4)
            
        with open(f'{searching_text_1}_не_найдено.json', 'w', encoding='utf_8_sig') as file:
            json.dump(items, file, ensure_ascii=False, indent=4)
            
        with open(f'{searching_text_1}ссылки.json', 'w', encoding='utf_8_sig') as file:
            json.dump(find_links, file, ensure_ascii=False, indent=4)  
            
        count += 1
    for i in items:
        console.print(f'{i} -- [red]текст не обнаружен[/red]')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    for i in info:
        console.print(f'{i} -- [green]текст обнаружен[/green]')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')
    for i in find_links:
        console.print(f'[green]{i}[/green]')
        
def start():
    
    answer = input('Введите тип парсинга(quick/slow): ')
    
    if answer == 'quick':
        parse()
    elif answer == 'slow':
        parse_with_links()
    else:
        print('Такого варината нет')
        start()
        
start()
    

        