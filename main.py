import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
votes = soup.select('.score')
links = soup.select('.titleline a')

base_url = 'https://news.ycombinator.com/'


def get_link_votes(linking, voting):
    hn = []
    for idx, item in enumerate(linking):
        link = item.get('href', None)
        if link and link.startswith('from?'):
            link = urljoin(base_url, link)
        title = item.getText()
        if idx < len(voting):
            points = int(voting[idx].get_text().replace(' points', ''))
            hn.append({'Title': title, 'Links': link, 'Points': points})
    return hn


def sort_stories(hack_news_list):
    return sorted(hack_news_list, key=lambda k: k['Points'], reverse=True)


hn_list = get_link_votes(links, votes)
pprint(sort_stories(hn_list))
