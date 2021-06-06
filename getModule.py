import requests
import re
from bs4 import BeautifulSoup


def findModule(moduleName):

    URL = 'https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(text=re.compile(moduleName))
    results = results.parent

    results = results.get('href')
    return results
    
    

