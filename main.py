#
# coding=utf-8

import sys
import os

from bs4 import BeautifulSoup as bsp
import urllib2

def test():
    proxy = urllib2.ProxyHandler({'http':'177.43.212.44'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/apple')
    if response is not None:
        html = response.read()
        print html
    else:
        print 'None'
    #
    soup = bsp(open("wiki_files/123.html"))
    print soup.title
    print soup.find_all('h2')

def add(a, b):
    return a+b

if __name__=='__main__':
    print test()
else:
    print test()