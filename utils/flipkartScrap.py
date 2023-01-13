
from urllib.request import urlopen
from utils import log

from bs4 import BeautifulSoup as bs
class FlipkartScrap:

    def __init__(self,url):
        self.url=url
        

    def get_data(url):
        page = urlopen(url)
        log.get_log("Url hitted")
        html_bytes = page.read()
  
        flipkart_html = bs(html_bytes, "html.parser")
        print(flipkart_html)

    

