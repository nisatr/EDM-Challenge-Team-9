import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com/page/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

df = []
for page in range(1,11):
    req = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    quote= soup.findAll('div', 'quote')

    for i in quote:
        isiQuotes = i.find('span', 'text').text
        authorName = i.find('small', 'author').text
        tags = [tag.text for tag in i.find_all('a', 'tag')]
    
        df.append([isiQuotes, authorName, ', '.join(tags)])

column = ['Isi Quotes', 'Author Quotes', 'Tags']
file = csv.writer(open('Mini Project 1/hasil-scraping.csv','w', newline='', encoding='utf-8'))   

file.writerow(column)
for x in df:
    file.writerow(x)