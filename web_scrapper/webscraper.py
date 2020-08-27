from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'lxml') # 'html.parser'
    print(bs.h1)
    

if __name__ == "__main__":
    main()




# CTRL + L                   Выделить строку
# CTRL + Shift + K           Удалить строку
# CTRL + Enter               Вставить строку снизу
# CTRL + Shift + Enter       Вставить строку свер
# Shift + Alt + A            Создать многострочный комментарий



