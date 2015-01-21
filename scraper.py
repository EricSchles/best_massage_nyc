import lxml.html
import requests
import grequests
import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("keyword")
args = parser.parse_args()
keyword = args.keyword

domains = pickle.load(open(".sites_to_scrape","r"))

rs = (grequests.get(u) for u in domains)
results = grequests.map(rs)
for r in results:
    html = r.text.decode("ascii","ignore")
    obj = lxml.html.fromstring(html)
    #gets all the hyper links
    links = [elem for elem in obj.xpath("//a/@href")] 
    
