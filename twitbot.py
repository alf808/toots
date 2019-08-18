'''This application will extract data from twitverse based on hashtag terms
or user's handle. This app uses BeautifulSoup and pyfiglet third-party modules.
Please see requirements.txt for other installation requirements. This was
tested using python 3.7.4.

Usage:
        python twitbot.py

Select from the menu options how you would like to interact with twitverse.
'''
import requests
from bs4 import BeautifulSoup
import sys
import pyfiglet
import string

def get_tweets(url, term, sym):
    '''Extract tweets based on term'''
    tweets = []
    results = requests.get(url,
       # params={'q':'%23' + hash_tag},
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'}
    )
    content = BeautifulSoup(results.text, 'html.parser')
    selected = content.select('div.tweet')
    #print(selected)
    c = 0
    fig = pyfiglet.figlet_format(f' {sym} {term}') # some ascii art
    print(fig)
    if len(selected) > 0:
        for tweet in selected:
            c += 1
            sel_name = tweet.select('strong.fullname')[0].get_text()
            sel_handle = tweet.select('span.username')[0].get_text()
            sel_pic = tweet.select('img.avatar')[0]['src']
            sel_tw = tweet.select('p.tweet-text')[0].get_text()
            output = f'{c}: {sel_name}, {sel_handle}, {sel_tw.strip()}, {sel_pic}'
            tweets.append(output)
        
        print(f"Here are top 5 tweets for {sym}{term}. See external file for full output.\n")
        print(*tweets[:5], sep='\n')

        strung = '\n'.join(tweets)
        with open('temp.txt', 'w') as fo:
            fo.write(strung)
    else:
        print('no results for that term')

def get_photos(url, term, sym):
    '''Extract tweets based on term'''
    tweets = []
    results = requests.get(url,
       # params={'q':'%23' + hash_tag},
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'}
    )
    content = BeautifulSoup(results.text, 'html.parser')
    selected = content.select('span.tweet-grid')
    #print(selected)
    c = 0
    fig = pyfiglet.figlet_format(f' {sym} {term}') # some ascii art
    print(fig)
    if len(selected) > 0:
        pass
        # for tweet in selected:
        #     c += 1
        #     sel_pic = tweet.select('img')[0]['src']
        #     output = f'{c}: {sel_pic}'
        #     tweets.append(output)
        #print(tweets)
        
        #print(f"Here are top 5 tweets for {sym}{term}. See external file for full output.\n")
        #print(*tweets[:5], sep='\n')

        #strung = '\n'.join(tweets)
        with open('temp.txt', 'w') as fo:
            fo.write(str(selected.children))
    #else:
     #   print('no results for that term')    

def get_full_report():
    '''Output the result of last query.'''
    try:
        with open('temp.txt') as fo:
            output = fo.read()
    except FileNotFoundError:
        print('Sorry the full output is not ready.')
    except:
        print('Sorry currently not handling the output file.')
    else:
        if output:
            print(output)
        else:
            print('\nno results for that term\n')


def elim_space(term):
    '''eliminate all white spaces
    https://www.journaldev.com/23763/python-remove-spaces-from-string
    '''
    output = term.translate({ord(c): None for c in string.whitespace})
    return output.lower()


def main():
    fig = pyfiglet.figlet_format("This is Twitbot")
    print(fig)
    print("We can get the latest tweets from twitverse -- by hashtag or user handle.")
    choice = "0"
    while True:
        print("\nMenu Choices:")
        print("(1) Tweets by Hashtag\t(2) Tweets by User\t(3) Tweets by Keyword\t(4) Tweets by image\t(f) Full output of last query\t(x) Exit")
        choice = input('Enter your choice: ')
        if choice == "1":
            type = input("Enter your hashtag: ")
            type = elim_space(type)
            get_tweets("https://twitter.com/search?q=%23" + type, type, '#')
        elif choice == "2":
            type = input("Enter user handle: ")
            type = elim_space(type)
            get_tweets("https://twitter.com/" + type, type, '@')
        elif choice == "3":
            type = input("Enter your keyword: ")
            get_tweets("https://twitter.com/search?q=" + type, type, '')
        elif choice == "4":
            type = input("Enter image keyword: ")
            get_photos("https://twitter.com/search?f=images&q=" + type, type, '')
        elif choice == "f":
            get_full_report()
        elif choice == "x":
            sys.exit("Bye")
        else:
            print("\nThat option is not currently supported.")


if __name__=="__main__":
    main()

