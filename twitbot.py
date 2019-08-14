import requests
from bs4 import BeautifulSoup
# import csv

url = "https://twitter.com/search"
tweets = []
results = requests.get(url,
    params={'q':'%23fredo'},
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'}
)
content = BeautifulSoup(results.text, 'html.parser')
# print(content)
selected = content.select('div.tweet')
print(selected)
c = 0
for tweet in selected:
    c += 1
    sel_name = tweet.select('strong.fullname')[0]
    sel_handle = tweet.select('span.username')[0]
    sel_pic = tweet.select('img.avatar')[0]
    sel_p = tweet.select('p.tweet-text')[0]
    tweets.append(f'{c}: {sel_p}, {sel_handle}, {sel_name}, {sel_pic}')
#     print(tweet)

strung = '\n'.join(tweets)

with open('temp.txt', 'w') as fo:
    fo.write(strung)
