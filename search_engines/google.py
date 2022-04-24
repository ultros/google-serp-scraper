import mechanize
import re


class GoogleRank:
    def __init__(self, url, domain, keyword):
        self.search_url = url
        self.rank_domain = domain
        self.rank_keyword = keyword
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko')
        ]
        self.br.addheaders = self.useragent

    def get_serp_links(self):
        self.br.open(self.search_url + self.rank_keyword)
        # print(self.search_url + self.rank_keyword)
        response = self.br.response().read()
        links = re.findall('href="/url\?.*?"><', str(response))

        parsed_link = []
        for link in links:
            split_link = link.split('=')
            split_link = link.split('https://')
            split_link = split_link[1].split('&')
            parsed_link.append(f"{split_link[0]}")

        return parsed_link

    def get_rank(self):
        i = 1
        ranked = []
        full_serp = []
        links = self.get_serp_links()
        for link in links:
            if link == f"www.{self.rank_domain}/" or link == f"{self.rank_domain}/" or link == f"www.{self.rank_domain}":
                text = f"You rank {i} for: {link} with keyword: {self.rank_keyword}"
                ranked.append(text)
            else:
                full_serp.append(f"{i}: {link}")
            i += 1
        return ranked, full_serp
