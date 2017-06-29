import requests
from bs4 import BeautifulSoup
import pprint as pp

"""ping url and return soup object"""
def get_soup(url):
	# TODO
	data = requests.get(url).text
	return BeautifulSoup(data, "html.parser")

# print(get_soup("http://cs50.tv"))


"""return page links if .html and not 'download'"""
def page_links(soup):
	# TODO
	a_s = soup.find_all('a', href=True)
	return [a['href'] for a in a_s if '.html' in a['href'] and 'download' not in a['href']]
	

"""hits cs50.tv for each year, concatonating all links"""
def all_pages():
	links = []
	for i in range(2007,2017):
		url = "http://cs50.tv/{yr}/fall/".format(yr=i)
		soup = get_soup(url)
		links += page_links(soup)
	return links

print(all_pages())