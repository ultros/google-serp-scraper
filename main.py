import argparse
import bs4
import requests
import re


def parse_links(your_domain, keyword):
    '''Finds and parses a list of the first Google SERP.'''
    fqdn_item_split = []
    response = requests.get(f"https://www.google.com/search?q={keyword}")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        parsed_link = re.findall('\A<a href="/url\?.*?;', str(link))

        if parsed_link:
            for parsed_url in parsed_link:
                if not re.search("google|youtube", str(parsed_url)):
                    fqdn = f"{parsed_url[24:-1]}"
                    fqdn_item = fqdn.split("/")
                    fqdn_item_split.append(fqdn_item[0])

    return fqdn_item_split


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
        if item == your_domain:
            print(f"{i}: {item} - You rank {i}  for \"{item}\" with keyword: {keyword}")
        else:
            print(f"{i}: {item}")

        i = i + 1


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Provide a keyword to search for (e.g. apline).")
    parser.add_argument("your_domain", help="The FQDN of your website (e.g. soundcloud.com).")
    args = parser.parse_args()
    get_rank(parse_sitelinks(parse_links(args.your_domain, args.keyword)), args.your_domain, args.keyword)