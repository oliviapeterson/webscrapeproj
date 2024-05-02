from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as plt
from plotly import offline

authors_list = []
quotes_list = []
tags_list = []
lengths = []  

# Scrape the first 10 pages of quotes
for page_number in range(1, 11):
    url = f'http://quotes.toscrape.com/page/{page_number}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    quotes = soup.findAll('div', class_='quote')
    
    for quote in quotes:
        author = quote.find('small', class_='author').text
        authors_list.append(author)        
        quote_text = quote.find('span', class_='text').text
        quotes_list.append(quote_text)        
        tags = quote.findAll('a', class_='tag')        
        for tag in tags:
            tags_list.append(tag.text)
        length = len(quote_text)  # Calculate length of the current quote
        lengths.append(length)  # Add length to the lengths list

# Author Statistics
author_dictionary = {}
for author in authors_list:
    if author in author_dictionary:
        author_dictionary[author] += 1
    else:
        author_dictionary[author] = 1

for author, count in author_dictionary.items():
    print(f"{author}: {count} quotes")

most_quotes_author = max(author_dictionary, key=author_dictionary.get)
least_quotes_author = min(author_dictionary, key=author_dictionary.get)

# Quote Analysis
average_length = sum(lengths) / len(lengths)
longest_quote = max(quotes_list, key=len)
shortest_quote = min(quotes_list, key=len)

# Tag Analysis
tag_counts = {}
for tag in tags_list:
    if tag in tag_counts:
        tag_counts[tag] +=1
    else:
        tag_counts[tag] = 1
most_popular_tag = max(tag_counts, key=tag_counts.get)
total_tags = len(tag_counts)

# Visualization
top_authors = sorted(author_dictionary, key=author_dictionary.get, reverse=True)[:10]
top_quotes = [author_dictionary[key] for key in top_authors]
top_tags = sorted(tag_counts, key=tag_counts.get, reverse=True)[:10]
top_tag_amounts = [tag_counts[key] for key in top_tags]

# Print Analysis Results
print("Author Statistics:")
print(f"Author with Most Quotes: {most_quotes_author}- {author_dictionary[most_quotes_author]} quotes")
print(f"Author with Least Quotes: {least_quotes_author}- {author_dictionary[least_quotes_author]} quotes")

print()
print("Quote Analysis:")
print()
print(f"Average Quote length: {average_length:.2f}")
print(f"Longest Quote: {longest_quote}")
print()
print(f"Shortest Quote: {shortest_quote}")
print()
print("Tag Analysis:")
print(f"Most Popular Tag: {most_popular_tag}")
print(f"Total Tags Used: {total_tags}")
data = [
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

my_layout = {
    'title':'Quotes by Authors',
    'xaxis':{"title":"Authors"},
    'yaxis':{'title':'Number of Quotes'}
}

fig_authors = {"data": data, "layout": my_layout}

offline.plot(fig_authors, filename='top_authors_quotes.html')
#tags

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