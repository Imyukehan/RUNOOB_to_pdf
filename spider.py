import requests
from bs4 import BeautifulSoup

start_url = 'http://www.runoob.com/php/php-tutorial.html'

def get_html(url):
    html = requests.get(url)
    return html.text

def get_next_url(html):
    soup = BeautifulSoup(html, 'lxml')
    next_url = soup.find('div', class_='next-design-link').find('a')
    return next_url['href']

def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    main_page = soup.find('div', class_='article-intro')
    return main_page
'''
def traverse(url):
    html = get_html(url)
    next_url = get_next_url(html)
    print(next_url)
    traverse(next_url)
'''

def main():
#    traverse(start_url)
    html = get_html(start_url)
    next_url = get_next_url(html)
    print(get_content(next_url))

if __name__ == '__main__':
    main()