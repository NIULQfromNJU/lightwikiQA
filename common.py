# Common configures
# -*- coding: utf-8 -*-

class Common(object):
    """A simple class for common usage"""
    downloadWikiFiles_path = 'downloadedWikiFiles'
    qaPairFiles_path = 'qaPairFiles'
    language = 'CHINESE'
    CN_suffix = ' - 维基百科，自由的百科全书.html'
    EN_suffix = ' - Wikipedia, the free encyclopedia.html'

    def __init__(self):
        self.downloadWikiFiles_path = 'downloadedWikiFiles'
        self.qaPairFiles_path = 'qaPairFiles'
        self.language = 'CHINESE'

    def get_downloadWikiFilesPath(self):
        return self.downloadWikiFiles_path

    def get_qaPairFilesPath(self):
        return self.qaPairFiles_path