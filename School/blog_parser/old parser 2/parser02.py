from bs4 import BeautifulSoup
import requests
import re
from rich.console import Console
import time

# Все ссылки для поиска
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
not_found_links = []

# Список с ифнормацией, так и не понял где он используется)
info = []
console = Console()

searching_list = [] 
      
        
def parse_with_links(items, find_links):
    
    for item in items:
        url = item
        
        req = requests.get(url, headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, 'lxml')

        links = soup.find_all('a')

        try:

            for link in links:
                req = requests.get(link.get('href'), headers=headers)
                src = req.text
                soup = BeautifulSoup(src, 'lxml')

                for keyword in searching_list:
                                
                    find_text = soup.find(text=re.compile(searching_list[keyword]))
                    
                    if find_text != None:
                        find_links.append(url)
                        items.remove(url)
                        break
                    elif link == links[-1]:
                        break
                    else:
                        pass                             
                                        
                            
        except Exception:
                    pass
                
    not_found_f = open(f'{searching_list[0]}_не_найдено.txt', "a")           
    found_f = open(f'{searching_list[0]}_найдено.txt', "a") 
    
    for i in find_links:         
        found_f.write(i + '\n')
    for i in items:
        not_found_f.write(i + '\n')
        
    found_f.close()
    not_found_f.close() 

def parse():
       
    for item in items:
        url = item
        
        req = requests.get(url, headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, 'lxml')

        for keyword in range(len(searching_list)):
            
            find_text = soup.find(text=re.compile(searching_list[keyword])) 
            
            if find_text != None:                
                find_links.append(url)
                items.remove(url)
                break
      
            else:
                pass
            
    not_found_f = open(f'{searching_list[0]}_не_найдено.txt', "a")           
    found_f = open(f'{searching_list[0]}_найдено.txt', "a") 
    
    for i in find_links:         
        found_f.write(i + '\n')
    for i in items:
        not_found_f.write(i + '\n')
        
    found_f.close()
    not_found_f.close() 
            
    print(find_links)
    print(items)
                
                
    parse_with_links(items, find_links)                          
               
                

        
def input_keywords():
    print("Для выхода из парсера введите: exit")
    print("Для перехода к парсингу введите: next \n")
    
    searching_list.clear()

    while True:    
        searching_text = input('Введите ключевое слово или словосочетание для поиска: ')

        if searching_text == 'next':
            break
        if searching_text == 'exit':
            exit("Досвидания!")           
        
        searching_list.append(searching_text)

def choose_parse():
    while True:
        answer = input('Начать парсинг?(yes/no): ')
        if answer == 'exit':
            exit("Досвидания!")
        if answer == 'yes':
            parse()
        elif answer == 'no':
            choose_parse()
        else:
            print('Такого варината нет')
            choose_parse()
        input_keywords()

def main():
    print("Здравствуйте!")

    input_keywords()
    choose_parse()
    
main() 