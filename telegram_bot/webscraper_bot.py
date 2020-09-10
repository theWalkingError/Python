from urllib.request import urlopen
from bs4 import BeautifulSoup

def rep_count(git_account_name):
    html = urlopen('https://github.com/' + git_account_name + '?tab=repositories')
    bs = BeautifulSoup(html.read(), 'html.parser')
    count_rep = bs.find('span', {'class':'Counter'})
    count = count_rep.get_text()
    return count

def rep_names(git_account_name):
    html = urlopen('https://github.com/' + git_account_name + '?tab=repositories')
    bs = BeautifulSoup(html.read(), 'html.parser')
    rep_names = bs.find_all('a', {'itemprop':'name codeRepository'})
    return rep_names

