import requests
from bs4 import BeautifulSoup
import sys
import pyfiglet


def get_tweets(url, term, sym):
    tweets = []
    results = requests.get(url,
       # params={'q':'%23' + hash_tag},
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'}
    )
    content = BeautifulSoup(results.text, 'html.parser')
    # print(content)
    selected = content.select('div.tweet')
    #print(selected)
    c = 0
    fig = pyfiglet.figlet_format(f'   {sym} {term}')
    print(fig)
    for tweet in selected:
        c += 1
        sel_name = tweet.select('strong.fullname')[0].get_text()
        sel_handle = tweet.select('span.username')[0].get_text()
        sel_pic = tweet.select('img.avatar')[0]['src']
        sel_tw = tweet.select('p.tweet-text')[0].get_text()
        output = f'{c}:{sel_name}, {sel_handle}, {sel_tw}, {sel_pic}'
        tweets.append(output)
    
    print("The latest 5 tweet samples. See external file for full output.\n")
    print(*tweets[:5], sep='\n\n')

    strung = '\n'.join(tweets)
    with open('temp.txt', 'w') as fo:
        fo.write(strung)


def main():
    fig = pyfiglet.figlet_format("This is Twitbot")
    print(fig)
    print("We can get the latest tweets from twitverse -- by hashtag or user handle.")
    choice = "0"
    while True:
        print("\nMenu Choices:")
        print("(1) Tweets by Hashtag\t(2) Tweets by User\t(x) Exit")
        choice = input('Enter your choice: ')
        if choice == "1":
            type = input("Enter your hashtag: ")
            get_tweets("https://twitter.com/search?q=%23" + type, type, '#')
        elif choice == "2":
            type = input("Enter user handle: ")
            get_tweets("https://twitter.com/" + type, type, '@')
        elif choice == "x":
            sys.exit("Thanks for wasting our time")
        else:
            print("\nThat option is not currently supported.")


if __name__=="__main__":
    main()

