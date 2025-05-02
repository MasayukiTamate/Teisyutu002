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

import wordcloudtest000

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



text = df4
text = "私はパイソンを学びます"
words = mecab_tokenizer(text)

font_path = "ZenMaruGothic-Black.ttf"

colormap="coolwarm"

wordcloud = WordCloud(font_path=font_path)
wordcloud.generate(words)


plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.show()

