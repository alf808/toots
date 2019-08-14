import requests
from bs4 import BeautifulSoup
import sys

def get_tweets(url):
    tweets = []
    #hash_tag = input("Enter hashtag to seasrch:  ")
    results = requests.get(url,
       # params={'q':'%23' + hash_tag},
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'}
    )
    content = BeautifulSoup(results.text, 'html.parser')
    # print(content)
    selected = content.select('div.tweet')
    #print(selected)
    c = 0
    for tweet in selected:
        c += 1
        sel_name = tweet.select('strong.fullname')[0].get_text()
        sel_handle = tweet.select('span.username')[0].get_text()
        sel_pic = tweet.select('img.avatar')[0]['src']
        sel_tw = tweet.select('p.tweet-text')[0].get_text()
        tweets.append(f'{c}:{sel_name}, {sel_handle}, {sel_tw}, {sel_pic}')
    #print(tweets)

    strung = '\n'.join(tweets)
    with open('temp.txt', 'w') as fo:
        fo.write(strung)


def main():
    choice = "0"
    while True:
        print("\nMenu Choices:")
        print("(1) Search Hashtag\t(2) Tweets by User\t(x) Exit")
        choice = input('Enter your choice: ')
        if choice == "1":
            type = input("Enter your hashtag: ")
            get_tweets("https://twitter.com/search?q=%23" + type)
        elif choice == "2":
            type = input("Input Username: ")
            get_tweets("https://twitter.com/" +type)
        elif choice == "x":
            sys.exit("Thanks for wasting our time")
    #else:
        # msg = random.choice(error_list)
        # print("\n" + msg)



if __name__=="__main__":
    main()

