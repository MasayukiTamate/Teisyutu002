import MeCab

CONTENT = "私はpythonを使用して、プログラミングを勉強しています。"

tagger = MeCab.Tagger()
parse = tagger.parse(CONTENT)

print(parse)