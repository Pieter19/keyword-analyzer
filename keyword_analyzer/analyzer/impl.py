import re
from typing import List, Dict

import requests
from bs4 import BeautifulSoup

url_regex = re.compile(  # Django url validator
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$',
    re.IGNORECASE
)


class ValidationError(Exception):
    pass


class FetchError(Exception):
    pass


def parse_url(url: str) -> BeautifulSoup:
    if not re.match(url_regex, url):
        raise ValidationError('URL is malformed, cannot proceed.')

    response = requests.get(url)

    if not response.ok:
        raise FetchError('Error fetching URL')

    soup = BeautifulSoup(response.content)

    return soup


def get_keywords(soup: BeautifulSoup) -> List:
    found = soup.find('meta', {'name': 'keywords'})

    if not found:
        return []

    tags = found.attrs['content']
    result = [tag.strip() for tag in tags.split(',')]

    return result


def search_for_keywords(soup: BeautifulSoup, keyword: str) -> int:
    found = soup.find_all(text=re.compile(keyword, re.IGNORECASE))
    return len(found)


def url_statistics(url:str) -> List[Dict]:
    soup = parse_url(url)
    keywords = get_keywords(soup)
    result = []
    for keyword in keywords:
        result.append({
            'keyword': keyword,
            'uses': search_for_keywords(soup, keyword)
        })

    return result
