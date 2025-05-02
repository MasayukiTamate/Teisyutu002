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



    mc = MeCab.Tagger()


    replaced_text = unicodedata.normalize("NFKC",text)
    replaced_text = replaced_text.upper()
    replaced_text = re.sub(r'[【】（）()『』「」]',"", replaced_text)
    replaced_text = re.sub(r'[\[\ [] \]]', ' ',replaced_text)
    replaced_text = re.sub(r'[@＠]\w+', "", replaced_text)
    replaced_text = re.sub(r'\d+\.*\d*', "", replaced_text)


    parsed_lines = mc.parse(replaced_text).split("\n")[:-2]

    surfaces = [l.split("\t")[0] for l in parsed_lines]
    pos = [l.split("\t")[1].split(",")[0] for l in parsed_lines]
    target_pos = ["名詞","動詞","形容詞"]
    token_list = [t for t, p in zip(surfaces, pos) if p in target_pos]

    kana_re = re.compile("^[あ-け]+$")
    token_list = [t for t in token_list if not kana_re.match(t)]

    return " ".join(token_list)

