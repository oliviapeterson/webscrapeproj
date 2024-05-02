from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as graph
from plotly import offline

authors_list = []
quotes_list = []
tags_list = []

page_number = 1

for page in range(1,11):
    url = f'http://quotes.toscrape.com/page/{page_number}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url,headers=headers)
    webpage = urlopen(req).read()          
    soup = BeautifulSoup(webpage, 'html.parser')
    quotes=soup.findAll('div', class_='quote')
#Quote
    for quote in quotes:
        author = quote.find('small', class_='author')
        authors_list.append(author)
        quote_text = quote.find('span', class_='text').text
        quotes_list.append(quote_text)
        tags = quote.findAll('a', class_='tag')
        for tag in tags:
            tags_list.append(tag.text)
    page_number += 1

#Author
author_dictionary = {}
most_quotes = 0
least_quotes = 100
author_most = ''
author_least = ''
for author in authors_list:
    if author in author_dictionary:
        author_dictionary[author]+=1
    else:
        author_dictionary[author] = 1

    count = author_dictionary[author]
    if count > most_quotes:
        author_most = author
        most_quotes = count

    if count < least_quotes:
        author_least = author
        least_quotes = count

print('Tag Statistics:')
dict_tags = {}
for tag in tags_list:
    if tag in dict_tags:
        dict_tags[tag] +=1
    else:
        dict_tags[tag] = 1

#Author and Quotes
top_authors = sorted(author_dictionary, key=author_dictionary.get, reverse=True)[:10]
top_quotes = [author_dictionary[key] for key in top_authors]
data_authors = [
    {
        'type': 'bar',
        'x': top_authors,
        'y':top_quotes,
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{"width":1.5,'color':'rgb(25,25,25)'},
        },
        'opacity':0.6,
    }
]

layout_tags = {
    'title':'Quotes by Authors',
    'xaxis':{"title":"Authors"},
    'yaxis':{'title':'Number of Quotes'}
}

fig_tags = {"data":data_authors, "layout":layout_tags}

offline.plot(fig_tags,filename='python_quotes.html')


#Tags______________
top_tags = sorted(dict_tags, key=dict_tags.get, reverse=True)[:10]
top_tag_amounts = [dict_tags[key] for key in top_tags]
data = [
    {
        'type': 'bar',
        'x': top_tags,
        'y':top_tag_amounts,
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{"width":1.5,'color':'rgb(25,25,25)'},
        },
        'opacity':0.6,
    }
]

my_layout = {
    'title':'Most Popular Tags by Author',
    'xaxis':{"title":"Tags"},
    'yaxis':{'title':'Count'}
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='python_tags.html')


