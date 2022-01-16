from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from rich.console import Console
import json
import csv

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
    "http://kadet-murmansk.ru/news",
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
    "http://murmanschool-37.ucoz.ru/index/novosti_2020_2021_uchebnogo_goda/0-377",
    "http://school38-murm.ru/content/blogcategory/165/203/",
    "https://sch41.murm.eduru.ru/news",
    "http://www.school42.znaet.ru/",
    "http://sc43murm.com.ru/index.php/novosti",
    "http://murman-school44.ru/",
    "https://sosh45.murm.eduru.ru/news",
    "https://school49.murm.eduru.ru/news",
    "http://school50.su/",
    "http://murmansk57.ru/",
    "http://www.school58.org.ru/"
]

searching_text = []
searching_text_1 = input('Введите первое ключевое слово для поиска: ')
searching_text_2 = input('Введите первое ключевое слово для поиска: ')
searching_text_3 = input('Введите первое ключевое слово для поиска: ')
searching_text_4 = input('Введите первое ключевое слово для поиска: ')

searching_text.extend([searching_text_1, searching_text_2, searching_text_3, searching_text_4])

console = Console()

info = []

def parse():
    
    count = 0
    while count != 4:
    
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }

        dict_count = 0

        for item in items:
            url = item
            
            req = requests.get(url, headers=headers, allow_redirects=False)
            src = req.text
            
            soup = BeautifulSoup(src, 'lxml')
                    
            find_text = soup.find_all(text=re.compile(searching_text[count]))  
                                   
            if find_text != []:

                try:
                                
                    if info[int(dict_count)].get(str(url)) == 'текст обнаружен':
                        print('Detected')
                        
                    elif info[int(dict_count)].get(str(url)) == 'текст не обнаружен':
                        console.print(f'{url}: [green]текст обнаружен[/green]')
                        info[dict_count] = {
                           f'{url}': 'текст обнаружен'  
                        }
                        
                except IndexError: 
                    console.print(f'{url}: [green]текст обнаружен[/green]')
                    info.append({
                        f'{url}': 'текст обнаружен' 
                    })
                        
            else:
                
                try:               
                    if info[int(dict_count)].get(str(url)) == 'текст не обнаружен':
                        pass
                    else: 
                        info.append({
                            f'{url}': 'текст не обнаружен' 
                        })
                        console.print(f'{url}: [red]текст не обнаружен[/red]')
                except IndexError:
                    console.print(f'{url}: [red]текст не обнаружен[/red]')
                    info.append({
                        f'{url}': 'текст не обнаружен' 
                    })
            
            dict_count += 1
            
        print(info)
                    
                                                
        with open(f'{searching_text}.json', 'w', encoding='utf_8_sig') as file:
            json.dump(info, file, ensure_ascii=False, indent=4)
            
        count += 1
      
parse()
    