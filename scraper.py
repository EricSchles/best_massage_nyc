import lxml.html
import requests
import grequests
import argparse
import sqlalchemy as sql

class Scraper:
    def __init__(self,testing=False):
        self.domains = ["http://manhattan.backpage.com/FemaleEscorts/"]
	self.testing = testing
    def run(self):
        ads = self._get_ads()
        pictures = []
        ad_texts = []
        for ad in ads:
            pictures.append(self._get_pictures(ad))#testing needed
            ad_texts.append(self_parse_ads(ad))#testing needed
            
    def _parse_ads(self,ad):
        html = lxml.html.fromstring(ad)
        text_obj = html.xpath("//div") #figure out what goes here.
        return [elem.text_content() for elem in text_obj][0] #this is a guess
        
    #save to db
    def _get_numbers(self):
        pass

    #testing needed
    def _get_pictures(self,ad):
        html = lxml.html.fromstring(ad)
        img_urls = html.xpath("//img/@src")
        imgs = []
        for url in img_urls:
            img_name = url.split("/")[-1]
            with open(img_name,"rb") as f:
                imgs.append(f.read())
        return imgs

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
            results = [elem.text.encode("ascii","ignore") for elem in results]
            return results
        else:
            rs = (grequests.get(u) for u in links)
            results = grequests.map(rs)
            results = [elem.text.encode("ascii","ignore") for elem in results]
            return results
            
