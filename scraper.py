import lxml.html
import requests
import grequests
import pickle
import argparse

class Scraper:
    def __init__(self):
        self.domains = pickle.load(open(".sites_to_scrape","r"))

    def run(self):
        ads = self._get_ads()

    def _parse_ads(self):
        pass

    #save to db
    def _get_numbers(self):
        pass
    def _get_pictures(self):
        pass
    def _get_locations(self):
        pass
    def _time_stamp(self):
        pass

    def _text_analysis(self):
        pass
    
    def _get_ads(self):
        rs = (grequests.get(u) for u in self.domains)
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
        return results
        
