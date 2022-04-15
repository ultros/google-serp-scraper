import argparse
import bs4
import requests
import re


def parse_links(your_domain, keyword):
    '''Finds and parses a list of the first Google SERP.'''
    full_link = []
    response = requests.get(f"https://www.google.com/search?num=100&q={keyword}")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        if link:
            parsed_link = re.findall('\A<a href="/url\?.*?"><', str(link))
            for link in parsed_link:
                sliced_link = link[24:-3]
                split_link = sliced_link.split('&amp')
                full_link.append(split_link[0])

    return full_link


def parse_sitelinks(fqdn_item_split):
    'Filter out Google Sitelinks.'
    prev_item = ""
    parsed_fqdn = []
    for item in fqdn_item_split:
        if item != prev_item:
            parsed_fqdn.append(item)
        prev_item = item

    return parsed_fqdn


def get_rank(parsed_fqdn, your_domain, keyword):
    '''Gets current pagerank of domain on Google Search Engine Results Page.'''
    i = 1
    for item in parsed_fqdn:
        link = item.split('/')
        if link[0] == your_domain:
            print(f"!!! {i}: {item}\n!!! You rank {i} for \"{item}\" with keyword: \"{keyword}\"")
        else:
            print(f"{i}: {item}  ")

        i = i + 1
    return


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Provide a keyword to search for (e.g. apline).")
    parser.add_argument("your_domain", help="The FQDN of your website (e.g. soundcloud.com).")
    args = parser.parse_args()
    get_rank(parse_sitelinks(parse_links(args.your_domain, args.keyword)), args.your_domain, args.keyword)