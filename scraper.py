import lxml.html
import requests
import grequests
import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("keyword")
args = parser.parse_args()
keyword = args.keyword # keyword must be /keyword/

domains = pickle.load(open(".sites_to_scrape","r"))

rs = (grequests.get(u) for u in domains)
results = grequests.map(rs)
final = []
links = []
for ind,r in enumerate(results):
    html = r.text.encode("ascii","ignore")
    obj = lxml.html.fromstring(html)
    #gets all the hyper links
    tmp = [elem for elem in obj.xpath('//div[@class="cat"]/a/@href')] 
    print tmp
    links += tmp

rs = (requests.get(u) for u in links)
results = grequests.map(rs)
print results[0].url
