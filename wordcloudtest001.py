import pandas as pd
import numpy as np
import unicodedata
import MeCab
from collections import Counter
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import ipadic
import re
from PIL import Image


def mecab_tokenizer(text):


    print(text)
    print(" ")
    mc = MeCab.Tagger()


    replaced_text = unicodedata.normalize("NFKC",text)
    print(replaced_text)
    print(" ")
    replaced_text = replaced_text.upper()
    print(replaced_text)
    print(" ")

    replaced_text = re.sub(r'[【】（）()『』「」]',"", replaced_text)
    print(replaced_text)
    print(" ")
    replaced_text = re.sub(r'[\[\ [] \]]', ' ',replaced_text)
    print(replaced_text)
    print(" ")
    replaced_text = re.sub(r'[@＠]\w+', "", replaced_text)
    print(replaced_text)
    print(" ")
    replaced_text = re.sub(r'\d+\.*\d*', "", replaced_text)
    print(replaced_text)
    print(" ")
    
    replaced_text = re.sub(r'# = .', "", replaced_text)
    print(replaced_text)
    print(" ")

    parsed_lines = mc.parse(replaced_text).split("\n")[:-2]
    print(parsed_lines)
    print(" ")
    surfaces = [l.split("\t")[0] for l in parsed_lines]
    print(surfaces)
    print(" ")
    pos = [l.split("\t")[1].split(",")[0] for l in parsed_lines]
    print(pos)
    print(" ")
    target_pos = ["名詞","動詞","形容詞"]

    token_list = [t for t, p in zip(surfaces, pos) if p in target_pos]
    print(token_list)
    print(" ")
    return " ".join(token_list)
'''
    kana_re = re.compile("^[あ-け]+$")
    print(kana_re)
    print(" ")

    token_list = [t for t in token_list if not kana_re.match(t)]
    print(token_list)
'''
#    return " ".join(token_list)


