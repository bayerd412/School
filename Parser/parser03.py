import re
from bs4 import BeautifulSoup
import requests
import csv
       
#Все ссылки для поиска
save_file_mode = 1
items = [
    "http://gymnaz1-murm.ru/",
    "http://2gimn51.ru/",
    "http://gym3murmansk.ucoz.ru/publ/?page1",
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

searching_list = [] 
find_items = []
find_links = []


def save_file_txt(find_items, items, find_links):

    not_found_f = open(f'{searching_list[0]}_не_найдено.txt', "a")           
    found_f = open(f'{searching_list[0]}_найдено.txt', "a") 
    found_f_links = open(f'{searching_list[0]}_ссылки.txt', "a")

    for i in find_items:         
        found_f.write(i + '\n')
    for i in items:
        not_found_f.write(i + '\n')
    for i in find_links:
        found_f_links.write(i + '\n')
        
    found_f.close()
    not_found_f.close() 
    found_f_links.close()


def save_file_csv(find_items, items, find_links):
    
    with open(f'{searching_list[0]}_не_найдено.csv', 'w', encoding='utf_8_sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item in items:
            writer.writerow([item])

    with open(f'{searching_list[0]}_найдено.csv', 'w', encoding='utf_8_sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for find_item in find_items:
            writer.writerow([find_item])

    with open(f'{searching_list[0]}_ссылки.csv', 'w', encoding='utf_8_sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for find_link in find_links:
            writer.writerow([find_link])
            

def choose_save_file_mode():
    global save_file_mode
    ask_save_file = input('Введите вид файла(csv/txt): ')

    if ask_save_file == 'csv':
        save_file_mode
        save_file_mode = 0
    elif ask_save_file == 'txt':
        save_file_mode
        save_file_mode = 1
    else:
        print('Такого режима нет')
        choose_save_file_mode()
        

def input_keywords():
    print("Для выхода из парсера введите: exit")
    print("Для перехода к парсингу введите: next \n")
    
    searching_list.clear()

    while True:    
        searching_text = input('Введите ключевое слово или словосочетание для поиска: ')
        searching_text_capitalized = searching_text.capitalize()

        if searching_text == 'next':
            break               
        elif searching_text == ':)':
            print('(-_-)')
        if searching_text == 'exit':
            exit("Досвидания!")           
        
        searching_list.append(searching_text) 
        searching_list.append(searching_text_capitalized)
        
        print(f'Список слов для поиска: {searching_list}\n\n')      
                
def parse_with_links(items, find_links):
    try:                         
        for item in items:
            req = requests.get(item)
            src = req.text
            
            soup = BeautifulSoup(src, 'lxml')
            
            links = soup.find_all('a')
                
            #Функция выхода из двух циклов сразу 
            def go_out_from_loops():       
                try:       
                    for link in links:
                        req = requests.get(link.get('href'))
                        src = req.text
                        
                        soup = BeautifulSoup(src, 'lxml')
                        
                        for keyword in range(len(searching_list)):
                            find_text = soup.find(text=re.compile(searching_list[keyword]))

                            if find_text != None:
                                items.remove(item)
                                find_items.append(item)
                                find_links.append(link.get('href'))
                                return
                            else:
                                pass                        
                except Exception:
                    pass       

            go_out_from_loops()
        
        if save_file_mode == 0:
            save_file_csv(find_items, items, find_links)
        else:
            save_file_txt(find_items, items, find_links)

    except Exception:
        pass
            
                        
def parse():
    for item in items:
        req = requests.get(item, headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, 'lxml')
        
        for keyword in range(len(searching_list)):
            
            find_text_link = soup.find('a', text=re.compile(searching_list[keyword]))
            find_text = soup.find(text=re.compile(searching_list[keyword]))
            
            if find_text_link != None:
                items.remove(item)
                find_items.append(item)
                if item in find_text_link.get('href'):
                    find_links.append(find_text_link.get('href'))
                    break
                else:
                    find_text_link = item + find_text_link.get('href')
                    find_links.append(find_text_link)
                    break

                break
            elif find_text != None:
                items.remove(item)
                find_items.append(item)
                find_links.append(item)
                break
            else:
                pass
            
    parse_with_links(items, find_links)
 
        
def main():
    input_keywords()
    choose_save_file_mode()
    parse()
    
    main()
       
main()