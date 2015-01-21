import lxml.html
import requests
import grequests
import pickle
from sys import argv


domains = pickle.load(open(".sites_to_scrape","r"))
print domains
