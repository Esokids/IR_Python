import pandas
import requests
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/—`'''
stop_words.update(punctuations)
df = pandas.read_csv("50web.csv", encoding='utf-8')


def invertedIndex():
    dic = defaultdict(list)
    # for i in range(len(df)):
    for i in range(3):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        data = soup.find("body").text.lower()
        tokens = set(sorted(word_tokenize(data)))
        tokens = [w for w in tokens if w not in stop_words]
        for word in tokens:
            dic[word].append(i+1)

    print(dic['sport'])


def positionalIndex():
    dic = defaultdict(list)
    # for i in range(len(df)):
    for i in range(3):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        content = soup.find("body").text.lower()
        tokens = word_tokenize(content)
        tokens = [w for w in tokens if w not in stop_words]
        tokens_set = list(set(tokens))

        for word in tokens_set:
            dic_pos = {}
            position = [j for j, x in enumerate(tokens, 1) if x == word]
            dic_pos[i+1] = position
            dic[word].append(dic_pos)

    for keys, values in [(keys, values) for x in dic['sport'] for (keys, values) in x.items()]:
        print(keys, values)
