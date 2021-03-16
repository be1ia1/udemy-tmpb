import requests
from bs4 import BeautifulSoup

start_url = 'https://www.rithmschool.com/blog?page=1'

response = requests.get(start_url)
soup = BeautifulSoup(response.text, 'html.parser')

# last_page_number = soup.find(class_="last").find('a')['href'][-1]

print(soup.find_all('article'))

# for i in range(1,last_page_number):


