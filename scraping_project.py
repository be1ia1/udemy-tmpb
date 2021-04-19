import requests
from bs4 import BeautifulSoup
from random import randint


def parse_page(soup):
    raw_quotes = soup.find_all(class_='quote')
    quote_list = []
    for raw_quote in raw_quotes:
        text = raw_quote.find(class_='text').get_text()
        author = raw_quote.find(class_='author').get_text()
        author_href = raw_quote.find('a')['href']
        quote_list.append([author, author_href, text])
    return quote_list


def get_quotes_info():
    all_quote_info = []
    url = 'http://quotes.toscrape.com/page/1/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    while soup.find(class_='next'):
        responce = requests.get(url)
        soup = BeautifulSoup(responce.text, 'html.parser')
        all_quote_info.extend(parse_page(soup))
        if soup.find(class_='next'):
            url = 'http://quotes.toscrape.com{}'.format(
                soup.find(class_='next').find('a')['href'])
    return all_quote_info


data = get_quotes_info()
guesses = []

while True:
    current_quote_data = data[randint(0, len(data) - 1)]
    quote_text = current_quote_data[2]
    quote_author = current_quote_data[0]
    author_page = 'http://quotes.toscrape.com{}'.format(current_quote_data[1])

    responce = requests.get(author_page)
    soup = BeautifulSoup(responce.text, 'html.parser')
    author_born = 'The author was born in '
    author_born += soup.find(class_='author-born-date').get_text()
    author_born += ', {}'.format(soup.find(class_='author-born-location').get_text())
    guesses.append("The author's last name start with {}".format(quote_author.split()[-1][0]))
    guesses.append("The author's first name start with {}".format(quote_author.split()[0][0]))
    guesses.append(author_born)

    print('Hint for testing: {}'.format(quote_author))

    print("Here's a quote:\n")
    print(quote_text)

    user_win = False
    user_answer = input('Who said this? ')

    while len(guesses) > 0:
        if user_answer == quote_author:
            user_win = True
            break
        hint = guesses.pop()
        user_answer = input("Here's is a hint: {} ".format(hint))

    if user_win:
        print('You win!')
    else:
        print('You lose!')
    user_again = input('Do you want play again? y/n ')
    if user_again == 'n':
        break
print('Good Luck!')