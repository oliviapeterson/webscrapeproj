import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapter = random.randrange(1,22)
if chapter<10:
    chapter = '0'+str(chapter)
else:
    chapter = str(chapter)
webpage = 'https://ebible.org/asv/JHN'+chapter+'.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('div', class_='p')

my_verses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('  ')
    #print(verse_list)

    for verse in verse_list:
        my_verses.append(verse)

my_verses = [i for i in my_verses if i != ' ']
mychoice = random.choice(my_verses)
print(f"Chapter:{chapter}")
print(f"Verse:{mychoice}")


