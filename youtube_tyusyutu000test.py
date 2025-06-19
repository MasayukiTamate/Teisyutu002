#　モジュールのインポート
from apiclient.discovery import build
from apiclient.errors import HttpError
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

import wordcloudtest001

# API情報
DEVELOPER_KEY = 'AIzaSyA4Oe6xjAJquiTIPS_Duawy1DTtXznNObE'   # ←準備で用意した各自のAPIキーを入力
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )
#検索ワード初期化
kensaku_kotoba = "vtuber"

#検索ワードで検索を実行
search_response = youtube.search().list(
  q=kensaku_kotoba,
  part='id,snippet',
  order='date',
  type='video',
  maxResults=50,
).execute()


df = pd.DataFrame(search_response["items"])
#各動画毎のvideoIdを取得
df1 = pd.DataFrame(list(df['id']))['videoId']
#各動画毎の動画情報取得
df2 = pd.DataFrame(list(df['snippet']))[['channelTitle','publishedAt','channelId','title','description']]
df4 = pd.DataFrame(list(df['snippet']))[['title',]]
# df1とdf2を結合
df3 = pd.concat([df1,df2], axis = 1)


#テキスト選別
text = ""
#アルファベットを含む文字列を排除
haijo_list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
haijo_list2 = []
for i in haijo_list1:
    haijo_list2.append(i.upper())
print("はじまりはじまり")
print("どうするか")
print(haijo_list1)

haijo_list3 = ["切り抜き",
              "V"
]
haijo_list4 = ["VTUBER"
]

#検閲エンジン
flag = False
for item in df4["title"]:
  strstr = item.split()
  for s in strstr:
    if not s[0] == "#":
      for i in haijo_list1:
         if not s[0] == i:
          for l in haijo_list2:
            if not s[0] == l:
              for j in haijo_list3:
                if not s[0] == j:
                  for k in haijo_list4:
                    if not s == k:
                      flag = True


    if flag:
      text = text + s + " "
      flag = False


words = wordcloudtest001.mecab_tokenizer(text)
print(words)

#ワードクラウド生成
font_path = "ZenMaruGothic-Black.ttf"
colormap="coolwarm"

wordcloud = WordCloud(
  width=1000,
  height=1000,
  font_path=font_path,

).generate(words)


plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.show()