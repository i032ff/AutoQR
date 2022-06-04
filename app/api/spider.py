import re
import requests
from bs4 import BeautifulSoup
    
def parse(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    iconURL = [url.attrs['href'] for url in soup.find_all('link', rel=re.compile('^.*icon.*$', re.IGNORECASE))]
    return iconURL