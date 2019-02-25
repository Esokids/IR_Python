import pandas
import requests
from BinarySearchTree import BST
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/—`'''
stop_words.update(punctuations)
df = pandas.read_csv("50web.csv", encoding='utf-8')


def invertedIndex(search="sported"):
    dic = defaultdict(list)
    # for i in range(len(df)):
    for i in range(10):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        data = soup.find("body").text.lower()
        tokens = word_tokenize(data)
        tokens = set([PorterStemmer().stem(token) for token in tokens])
        tokens = [w for w in tokens if w not in stop_words]
        for word in tokens:
            dic[word].append(i+1)
    search = word_tokenize(search)
    search = [PorterStemmer().stem(word) for word in search]
    search = [w for w in search if w not in stop_words]

    print(Intersect_word(dic, search))
    return Intersect_word(dic, search)


def Intersect_word(dic, search):
    if len(search) == 1:
        result = dic[search[0]]
    else:
        i = 1
        result = []
        for word in search:
            if i == 1:
                temp = set(dic[word])
                i += 1
            else:
                result = set(dic[word])
                temp = temp & result
                result = temp
    result = [df['Link'][index] for index in result]
    return result


def positionalIndex():
    dic = defaultdict(list)
    # for i in range(len(df)):
    for i in range(3):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        content = soup.find("body").text.lower()
        tokens = word_tokenize(content)
        tokens = [PorterStemmer().stem(token) for token in tokens]
        tokens = [w for w in tokens if w not in stop_words]
        tokens_set = list(set(tokens))

        for word in tokens_set:
            dic_pos = {}
            position = [j for j, x in enumerate(tokens, 1) if x == word]
            dic_pos[i+1] = position
            dic[word].append(dic_pos)

    for keys, values in [(keys, values) for x in dic['sport'] for (keys, values) in x.items()]:
        print(keys, values)

    ''''' **** same ****
    # for x in dic['sport']:
    #     for key, value in x.items():
    #         print(key, value)
    #         print(type(keys), type(value))
    '''''


def binarySearchTree():
    dic = defaultdict(list)
    bst = BST()
    # for i in range(len(df)):
    for i in range(3):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        data = soup.find("body").text.lower()
        tokens = set(word_tokenize(data))
        tokens = [w for w in tokens if w not in stop_words]
        tokens = sorted(tokens)
        for word in tokens:
            dic[word].append(i + 1)

    print(dic)

    # for e in dic:
    #     bst.insert(e)

    # print(bst.find('sport'))


'''''
def testBST():
    bst = BST()
    # arr = sorted([1,2,3,4,5,6,7,8,9,0])
    # arr = sorted(['a','b','c','d','e','f','g','h','i','j','aa'])
    arr = {'a':[1,2], 'b':[1], 'c':[2], 'd':[3], 'e':[4,5]}
    for value in arr.items():
        bst.insert(value)
        print(value)

    # print(bst.find(10))
    # print(bst.find('aa'))
    print(bst.find('a'))
'''''


def hash_Dictionary(search):
    dic = defaultdict(list)
    # for i in range(len(df)):
    for i in range(3):
        url = df['Link'][i]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        data = soup.find("body").text.lower()
        tokens = set(word_tokenize(data))
        tokens = [w for w in tokens if w not in stop_words]
        tokens = sorted(tokens)

        for word in tokens:
            dic[word].append(i+1)
    search = PorterStemmer().stem(search)
    result = [df['Link'][index] for index in dic[search]]
    return result


if __name__ == '__main__':
    invertedIndex()
    # positionalIndex()
    # binarySearchTree()
    # testBST()
