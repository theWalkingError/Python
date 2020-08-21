from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver.get('https://линуксблог.рф/parsing-sajtov-na-python-chast-1/')
    botton = driver.find_element_by_id("menu-item-451")
    botton.click()
    
    

if __name__ == "__main__":
    main()