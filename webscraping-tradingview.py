from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



url = 'https://www.webull.com/quote/us/gainers/1d'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

stock_data = soup.findAll("div", attrs={"class":"table-cell"})
print(stock_data[1].text)
print(stock_data[12].text)
counter = 1
for x in range(5):
    name = stock_data[counter]
    change = float(stock_data[counter+2].text.strip("%".strip("+")))
    last_price = float(stock_data[counter+3]).text()
    previous_price = round(last_price/ ((1+change)/100) ,2)
    print(f"Company Name: {name}")
    print(f"Change: {change}")
    print(f"Price: {last_price}")
    print(f"Previous Price: {previous_price}")




#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

