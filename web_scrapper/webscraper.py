from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from selenium import webdriver
import os

def main():

    def get_title(url):
        try:
            html = urlopen(url)   
            try:
                bs = BeautifulSoup(html.read(), 'lxml') # вместо 'lxml' можно использовать 'html.parser'
                title = bs.body.h2

                return title

            except AttributeError as e:
                return None 
        except HTTPError as error:
            return None
        except URLError as e:
            print(e)

    def get_smth(url):
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'lxml')
        titleList = bs.findAll('div', {'class':'entry-content'})  
        new_title = titleList.bs.h2   
        for title in new_title:
            print(title.get_text()) 


    # title = get_title('https://tproger.ru/translations/guide-into-python-imports/#11')
    # if title == None:
    #     print('Error')
    # else:
    #     print(title)


    # get_smth('https://python-scripts.com/redis')
    
    click_try("https://github.com/theWalkingError")

if __name__ == "__main__":
    main()




# CTRL + L                   Выделить строку
# CTRL + Shift + K           Удалить строку
# CTRL + Enter               Вставить строку снизу
# CTRL + Shift + Enter       Вставить строку свер
# Shift + Alt + A            Создать многострочный комментарий


