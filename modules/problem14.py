from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_data(url):
    response = urlopen(url)
    content= response.read()
    return content

def get_all_links(link):
    html = get_data(link)

    soup = BeautifulSoup(html, 'html.parser')

    all_links = soup.find_all('a')
    return [ link.get('href') for link in all_links ]

url = "https://www.lipsum.com/"
print(get_all_links(url))