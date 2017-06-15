import requests
import pdfkit
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

def save_html(html):
    with open('index.html', 'a') as f:
        f.write(str(html))



def save_pdf(htmls):
    '''
    把所有html文件转换成pdf文件
    '''
    file_name = 'php.pdf'
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options)

times = 1

def traverse(url):
    print(url)
    html = get_html(url)
    next_url = get_next_url(html)
    page = get_content(next_url)
    save_html(page)
    global times
    times += 1
    if times > 70:
        return

    traverse(next_url)


def main():
    #traverse(start_url)
    save_pdf('index.html')
    

if __name__ == '__main__':
    main()