import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/search"

results = requests.get(url, params={'q':'cybersecurity'})
soup = BeautifulSoup(results.text, 'html5lib')
print(soup.prettify())

# users = soup.select("div.tweet a.js-user-profile-link")

usernames = soup.select("div.tweet strong.fullname")
for un in usernames:
    print(un.text)
