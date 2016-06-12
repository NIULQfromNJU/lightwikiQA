# used to parse a wiki page
# by niuliqiang
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bsp

# class
class ParseWikiPage(object):
    absolute_wiki_file = ''
    qa_file = ''

    def __init__(self, a_w_f):
        self.wiki_file = a_w_f
        self.qa_file = ''

    def Parse(self):
        print self.absolute_wiki_file
        return 0
