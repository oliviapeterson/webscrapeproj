#Find a 'scrappable' cryptocurrencies website where you can scrape the
#top 5 cryptocurrencies and display as a formatted output one currency at a time.
#The output should display the name of the currency, the symbol (if applicable),
#the current price and % change in the last 24 hrs and corresponding price (based on % change)

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)
print()
td = soup.findAll("td")
counter = 1

for row in range(5):
    name = td[counter+1].text
    price = float(td[counter+2].text.strip('$').replace(',', ''))
    percent_change = float(td[counter+4].text.strip('^').strip('%'))
    original_price = (price * percent_change,2)
    original_price = price + (price * (percent_change / 100))
    print(f"{name} ${price} {percent_change} {price}")
    print()
    counter += 11
