# #theses tests are inspired by: https://github.com/EricSchles/syncano-python/blob/master/tests.py

# #usage: nosetests tests.py //passing :)
# import unittest
# import urllib2
# import logging
# from scraper import Scraper

# logging.basicConfig(filename="tests.log", level=logging.INFO)

# def internet_on(addr):
#     try:
#         response = urllib2.urlopen(addr,timeout=20)
#         return True
#     except urllib2.URLError as err: pass
#     return False

# # class ScraperSetupTest:

# #     def setup(self):
# #         addrs = ["https://www.google.com","https://www.microsoft.com","https://www.apple.com"]
# #         for addr in addrs:
# #             if not internet_on(addr): 
        
# class TestScraper(unittest.TestCase):
    
#     def test_connection(self):
#         addrs = ["https://www.google.com","https://www.microsoft.com","https://www.apple.com"]
#         for addr in addrs:
#             if not internet_on(addr):
#                 assert False
#     def test_one(self):
#         s = Scraper(testing=True)
#         if not s.run(): assert False
        
