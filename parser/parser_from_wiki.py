import textwrap

import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {'user_agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)', 'accept': '*/*'}
PATH = "C:\\Users\\vladw\PycharmProjects\python_tests\parser\\texts"


class ParserFromWiki:
    def __init__(self, url):
        self.url = url

        self.html_text = requests.get(self.url).text
        self.current_date = str(datetime.today().strftime('%d.%m.%Y'))
        self.soup = BeautifulSoup(self.html_text, 'html.parser')

    def get_html(self, params=None):
        # return html code of url
        r = requests.get(self.url, headers=HEADERS, params=params)
        return r

    def check_conn(self):
        # return status code
        html = self.get_html(self.url)
        return html.status_code

    # not used
    def get_all_text(self):
        # return all html text
        html_text = requests.get(self.url).text
        return html_text

    def get_h1_title(self):
        return self.soup.find('h1').text

    def get_link(self):
        name_str = self.get_h1_title().replace(' ', '_')
        wiki_str = str(self.url).replace('https://', '')[:16]
        res_str = f"{wiki_str}/wiki/{name_str}"
        return res_str

    def get_current_time(self):
        return self.current_date

    def get_result(self):
        result = f"{self.get_h1_title()} [Электронный ресурс] /. - Электрон.текстовые дан. " \
                 f"- Режим доступа: {self.get_link()}, свободный (дата обращения {self.get_current_time()})"
        return result


if __name__ == "__main__":
    url = str(input("Введите ссылку на сайт:"))
    parser = ParserFromWiki(url)
    if parser.check_conn() == 200:
        print(parser.get_result())
    else:
        print("Error")
