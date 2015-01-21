import lxml.html
import requests
#import grequests
#import pickle
import argparse
import sqlalchemy as sql

class Scraper:
    def __init__(self,testing=False):
        #self.domains = pickle.load(open(".sites_to_scrape","r"))
	self.testing = testing
        #db stuff:
        self.engine = sql.create_engine("sqlite://:memory",echo=True)
        self.Base = sql.ext.declarative.declarative_base()
        
    def run(self):
        ads = self._get_ads()
        _get_pictures(self,ads)
        
        if self.testing:
            return ads
    def _parse_ads(self):
        pass

    #save to db
    def _get_numbers(self):
        pass
    def _get_pictures(self,ads):
        for ad in ads:
            
        
        if self.testing:
            return True #make this an actual state.
        
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
            
            links += tmp
        
        if self.testing:
            rs = (grequests.get(u) for u in links[:5])
            results = grequests.map(rs)
        
            return results
        else:
            rs = (grequests.get(u) for u in links)
            results = grequests.map(rs)
        
            return results
            
