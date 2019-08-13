import requests
from bs4 import BeautifulSoup
# import csv

url = "https://twitter.com/pattonoswalt"
tweets = []
results = requests.get(url)
content = BeautifulSoup(results.text, 'html5lib')

selected = content.select('div.tweet')
c = 0
for tweet in selected:
    c += 1
    sel_p = tweet.select('p.tweet-text')[0].get_text()
    tweets.append(f'{c}: {sel_p}')
    # print(sel_p)
strung = '\n'.join(tweets)

with open('temp.txt', 'w') as fo:
    fo.write(strung)
