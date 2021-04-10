# -*- coding: utf-8 -*-

'''
各种分词器的实现
'''

import re
import jieba


class CutByJieba:
    ''' 基于jieba分词的分词器 '''

    def __init__(self, enable=True):
        self.enable = enable
        if enable:
            jieba.enable_paddle()

    def cut_words(self, line: str) -> str:
        seg_list = jieba.cut(line, use_paddle=self.enable)
        return ' '.join(list(seg_list))


class CutByBlank:
    ''' 根据空格分词 '''

    def __init__(self):
        self.re_trim = re.compile(r'\s+')

    def cut_words(self, line: str) -> str:
        return self.re_trim.sub(' ', line)
