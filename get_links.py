import pprint as pp
import requests

from bs4 import BeautifulSoup

def get_soup(url):
    """ping url and return soup object"""
    data = requests.get(url).text
    return BeautifulSoup(data, "html.parser")


def page_links(soup):
    """return page links if .html and not 'download'"""
    a_s = soup.find_all('a', href=True)
    return [a['href'] for a in a_s if '.html' in a['href'] and 'download' not in a['href']]
    

def all_pages():
    """hits cs50.tv for each year, concatonating all links"""
    links = []
    for i in range(2007,2017):
        url = "http://cs50.tv/{yr}/fall/".format(yr=i)
        soup = get_soup(url)
        links += page_links(soup)
    return links


print(all_pages())
