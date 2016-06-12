# pipeline for question answering
# -*- coding: utf-8 -*-

import sys
import os

class LightQAPipeline(object):
    """A simple class for Wiki-based lightQA Pipeline"""
    question = ''
    keyword = ''
    answer = ''

    def __init__(self, question):
        self.question = question
    #
    # step-1: parse input question & extract keywords
    def ParseQuestion(self):




# Test LightQAPipeline
if __name__=='__main__':
    test_question1 = '梨是什么？'
    test_question2 = '梨有哪些营养？'
    test_question3 = '梨有哪些相关故事？'
    qaPipeline = LightQAPipeline(test_question1)




