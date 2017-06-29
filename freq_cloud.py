import requests
from bs4 import BeautifulSoup
import re
from links import links
links = links[-1:]


"""ping url and return soup object"""
def get_soup(url):
	data = requests.get(url).text
	return BeautifulSoup(data, "html.parser")


"""return all relevant text as continuous string"""
def text(soup):
	# TODO
	return


"""convert all strings to lower and remove irrelevant chars like .;'"""
def clean(raw_text):
	return [s.lower() for s in re.split(" |\"|\,|\;|\.|\'|\)|\(", raw_text) if s != ""]


"""Determines how much we care about length of tuple vs. its frequency"""
def weight_fn(x):
	return len(x[0].split(' ')) * x[1]


"""return top phrases (tuples) with their frequencies"""
def frequent_phrases(arr, tup=6, size=100):
	dict = {}
	tuples = ['' for i in range(tup)]
	for i, word in enumerate(arr):
		tuples = [tuple + ' ' + word for tuple in tuples]
		for tuple in tuples:
			if tuple in dict:
				dict[tuple] += 1
			else:
				dict[tuple] = 1
		idx = i % tup
		# tuple = tuples[idx]
		tuples[idx] = ''
	freq_map = []
	for phrase in dict:
		freq_map.append([phrase, dict[phrase]])
	return sorted(freq_map, key=weight_fn,reverse=True)[:size]


"""prints an html word cloud of the most frequent phrases"""
def cloud(freq_phrases):
	# TODO
	return

"""Does cloud generation after hitting all pages"""
def main(links):
	arr = []
	for page in links:
		soup = get_soup(page)
		raw_text = text(soup)
		arr += clean(raw_text)
	freq_phrases = frequent_phrases(arr)
	cloud(freq_phrases)

# main(links)
