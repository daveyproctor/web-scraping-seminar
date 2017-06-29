import re
import requests

from bs4 import BeautifulSoup
from links import links

links = links[-5:]


def get_soup(url):
    """ping url and return soup object"""
    data = requests.get(url).text
    return BeautifulSoup(data, "html.parser")


def text(soup):
    """return all relevant text as continuous string"""
    all_paras = soup.find_all('p')
    return ' '.join([para.get_text() for para in all_paras])


def clean(raw_text):
    """convert all strings to lower and remove irrelevant chars like .;'"""
    return [s.lower() for s in re.split(" |\"|\,|\;|\.|\'|\)|\(", raw_text) if s != ""]


def weight_fn(x):
    """Determines how much we care about length of tuple vs. its frequency"""
    return len(x[0].split(' ')) * x[1]


def freq_phrases(arr, tup=6, n=100):
    """return top phrases (tuples) with their frequencies"""
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
        tuples[idx] = ''
    freq_map = []
    for phrase in dict:
        freq_map.append([phrase, dict[phrase]])
    return sorted(freq_map, key=weight_fn,reverse=True)[:n]


def cloud(freq_phrases):
    """prints an html word cloud of the most frequent phrases"""
    for phrase in freq_phrases:
        try:
            print("<div style=\"font-size: {0}px\"> {1} </div>".format(weight_fn(phrase), phrase[0]))
        except UnicodeEncodeError:
            pass


def main(links):
    """Does cloud generation after hitting all pages"""
    arr = []
    for page in links:
        soup = get_soup(page)
        raw_text = text(soup)
        arr += clean(raw_text)
    freq_phrases = freq_phrases(arr)
    cloud(freq_phrases)


main(links)






