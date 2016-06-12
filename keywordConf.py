# configure for  keywords
# -*- coding: utf-8 -*-

import os
import sys

from common import Common

class KeywordConfig(object):
    """A simple class for Keyword Configure"""
    # Wiki 关键字 或者 关键词语
    keyword = ''
    # 关键字 关联的 wiki html文件
    keyword_wiki_file = ''
    #
    absolute_keyword_wiki_file = ''

    def __init__(self, kw):
        self.keyword = kw
        if Common.language == 'CHINESE':
            self.keyword_wiki_file = self.keyword + Common.CN_suffix
        elif Common.language == 'ENGLISH':
            self.keyword_wiki_file = self.keyword + Common.EN_suffix
        else:
            print 'Language Error!'
            sys.exit(-1)
        print 'keyword: ', self.keyword
        print 'wiki_file: ', self.keyword_wiki_file

    def printKeyword(self, kw):
        print self.keyword

    # 检测 关键字wiki页面是否已存在
    def CheckKeywordDownloadedWikiFile(self):
        absolute_path = os.path.join(os.getcwd(), Common.downloadWikiFiles_path)
        print absolute_path
        if os.path.exists(absolute_path):
            absolute_file_path = os.path.join(absolute_path, self.keyword_wiki_file)
            # print absolute_file_path
            unicode_absolute_file_path = absolute_file_path.decode('utf-8')
            # print unicode_absolute_file_path
            if os.path.isfile(unicode_absolute_file_path):
                self.absolute_keyword_wiki_file = unicode_absolute_file_path
                print 'Keyword Wiki File Existed!'
                return True
            else:
                print 'Keyword Wiki File Not Existed!'
                return False
        else:
            print 'DownloadedWikiFiles Path Not Existed!'
            return False
    #

if __name__=='__main__':
    kc = KeywordConfig('梨')
    kc.CheckKeywordDownloadedWikiFile()




