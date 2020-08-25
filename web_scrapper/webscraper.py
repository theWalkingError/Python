from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
    

if __name__ == "__main__":
    main()