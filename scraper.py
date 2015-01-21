import lxml.html
import requests
import grequests
import pickle
from sys import argv


domains = pickle.load(open(".sites_to_scrape","r"))

rs = (grequests.get(u) for u in domains)
results = grequests.map(rs)
for r in results:
    
