import textwrap

import requests
import copy
import re
from bs4 import BeautifulSoup

URL = ""
HEADERS = {'user_agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)', 'accept': '*/*'}
PATH = "C:\\Users\\vladw\PycharmProjects\python_tests\parser\\texts"
CONTENT_TAGS = ["p"]
WRAP = 80


def get_html(url, params=None):
    # return html code of url
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(url):
    # return clear text of article
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    content = soup.find_all(CONTENT_TAGS)

    # Getting the entire tag content, described in self.content_tags.
    wrapped_text = ""
    for p in content:
        # Skipping empty tags.
        if p.text != "":
            # Formatting links into view: [link]
            links = p.find_all('a')
            if links != "":
                for link in links:
                    p.a.replace_with(str("[" + link['href'] + "]"))
            # Text formatting in tags according to сolumn width.
            wrapped_text += "".join(textwrap.fill(p.text, WRAP)) + "\n\n"
    save_text(wrapped_text)


def save_text(text):
    file = open(PATH, 'w')
    file.write("\n---------Новая статья---------\n\n" + text)
    file.close()
    print("Запись совершена успешно!")


def parse(url):
    # main func
    html = get_html(url)
    print(html.status_code)
    if html.status_code == 200:
        get_content(url)
    else:
        print("Error")


if __name__ == "__main__":
    print("Введите URL адрес:")
    URL = input()
    parse(URL)
