import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Success code is 200
print(r)

# It use to print content of website
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div' , class_="text")
content = s.find_all('p')
print(content)
