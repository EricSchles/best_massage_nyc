import lxml.html
import requests
import grequests
import pickle
from sys import argv


domains = pickle.load(open(".sites_to_scrape","r"))

rs = (grequests.get(u) for u in domains)
results = grequests.map(rs)
for r in results:
    html = r.text.decode("ascii","ignore")
    obj = lxml.html.fromstring(html)
    #gets all the hyper links
    links = [elem for elem in obj.xpath("//a/@href")] 
    
