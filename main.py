import bs4
import requests
import re

# .... ....

keyword = "jesse shelley"
url = f"https://www.google.com/search?q={keyword}"
your_page = "zildjian.com"


response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

i = 0
'''Add FQDN to new list.'''
fqdn_item_split = []
for link in links:
    parsed_link = re.findall('\A<a href="/url\?.*?;', str(link))

    if parsed_link:
        for parsed_url in parsed_link:
            if not re.search("google|youtube", str(parsed_url)):
                fqdn = f"{parsed_url[24:-1]}"
                fqdn_item = fqdn.split("/")
                fqdn_item_split.append(fqdn_item[0])

'''Filter out Google Sitelinks.'''
prev_item = ""
parsed_fqdn = []
for item in fqdn_item_split:
    if item != prev_item:
        parsed_fqdn.append(item)
    prev_item = item

i = 0
for item in parsed_fqdn:

    if item == your_page:
        print(f"{i+1}: {item} - You rank {i+1}  for \"{item}\"")
    else:
        print(f"{i+1}: {item}")

    i = i + 1
