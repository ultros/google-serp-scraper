from search_engines import google
import argparse


def get_google_rank(rank_domain, rank_keyword):
    search_url = 'https://www.google.com/search?num=100&q='
    gr = google.GoogleRank(search_url, rank_domain, rank_keyword)
    ranked, full_serp = gr.get_rank()
    for position in ranked:
        print(position)
    # print(full_serp)


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    google = subparser.add_parser('google')
    google.add_argument('--domain', type=str, required=True)
    google.add_argument('--keyword', type=str, required=True)

    args = parser.parse_args()

    if args.command == 'google':
        get_google_rank(args.domain, args.keyword)


if __name__ == '__main__':
    main()
