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
final = []
links = []
for ind,r in enumerate(results):
    html = r.text.encode("ascii","ignore")
    obj = lxml.html.fromstring(html)
    #gets all the hyper links
    tmp = [elem for elem in obj.xpath("//a/@href")] 
    links += tmp
print len(links)
for link in links:
    if keyword in link and not "http" in link:
        domain = domains[ind].split(keyword)[0] #keyword cannot be domain
        r = requests.get(domains[ind]+link)
        final.append(r)
        print r.url

print final[0].url
