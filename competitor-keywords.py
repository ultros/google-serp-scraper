from search_engines import google
import argparse
import bs4
import requests


def get_keywords(keyword):
    soup = bs4.BeautifulSoup()
    search_url = 'https://www.google.com/search?num=100&q='
    rank_domain = ""
    rank_keyword = keyword
    gr = google.GoogleRank(search_url, rank_domain, rank_keyword)
    link_list = gr.get_serp_links()

    prior_link = ""
    keyword_list = []
    description_list = []
    for link in link_list:
        if prior_link != link:
            response = requests.get(f"http://{link}")
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            keywords = soup.findAll(attrs={"name": "keywords"})
            if keywords:
                print(keywords)
                keyword_list.append(keyword)
            else:
                pass
        else:
            pass  # duplicates?
        prior_link = link



def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    google = subparser.add_parser('google')
    google.add_argument('--keyword', type=str, required=True)
    args = parser.parse_args()

    if args.command == 'google':
        get_keywords(args.keyword)


if __name__ == '__main__':
    main()
