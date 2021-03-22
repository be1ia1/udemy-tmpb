import requests
from bs4 import BeautifulSoup

start_url = 'https://www.rithmschool.com/blog?page=1'

response = requests.get(start_url)
soup = BeautifulSoup(response.text, 'html.parser')

last_page_number = int(soup.find(class_="last").find('a')['href'][-1])


def get_info(url_page):
    data = []
    for article in soup.find_all('article'):
        title = article.find('a').get_text()
        href = article.find('a')['href']
        pub_date = article.find('time').attrs['datetime']
        data.append([href, title, pub_date])
    return data


for i in range(1, last_page_number):
    url_page = 'https://www.rithmschool.com/blog?page={}'.format(i)
    print(get_info(url_page))
