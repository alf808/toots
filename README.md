# Toots: sample application to scrape web data and provide a basic sentiment analysis

This application will extract data from twitverse based on hashtag terms
or user's handle. It will also attempt to give a sentiment analysis of
each tweet and the topic in general. It uses BeautifulSoup, textblob,
and pyfiglet third-party modules.

Please see requirements.txt for other installation requirements. This was
tested using python 3.7.4.

## Usage:
```
python3 twitbot.py
```
Select from the menu options how you would like to interact with twitverse.

## Requirements:

python version: Python 3.7.4

python modules:

1. requests
1. BeautifulSoup
1. pyfiglet
1. textblob
1. sqlite3

## Resources:

- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://dev.to/ayushsharma/a-guide-to-web-scraping-in-python-using-beautifulsoup-1kgo
- https://www.journaldev.com/23763/python-remove-spaces-from-string
- https://realpython.com/python-requests/#request-headers
- https://textblob.readthedocs.io/en/dev/