import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Dead_by_Daylight"

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup('a')

    citation_count = 0
    for link in links:
        if link.get('title') == "Wikipedia:Citation needed":
            citation_count += 1

    return citation_count

def get_citations_needed_report(url):
    report = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    p_tags = soup('p')

    for p in p_tags:
        links = p('a')
        for link in links:
            if link.get('title') == "Wikipedia:Citation needed":
                report += p

    return report

# testing
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
p_tags = soup('p')

for p in p_tags:
    links = p('a')
    for link in links:
        if link.get('title') == "Wikipedia:Citation needed":
            print(p)


# if __name__ == '__main__':
#     print(get_citations_needed_report(URL))