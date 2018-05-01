import scrapy
from debike.items import Station

from datetime import datetime

class ToScrapeJsGyn(scrapy.Spider):
    name = 'toscrape-js-gyn'
    start_urls = ['https://www.mobilicidade.com.br/bikegoiania/mapaestacao.aspx']

    def parse(self, response):
        # Parse <script>
        station = response.xpath('//script').re('var beaches = (.*);')
        
        # Str to Array
        station = eval(station[0])

        for s in station:
          item = Station()

          item['name']    = s[0]
          item['address'] = s[3]
          item['lat']     = float(s[1])
          item['lng']     = float(s[2])
          
          item['available'] = int(s[8])
          item['free']    = int(s[9])

          item['status']  = s[5]
          item['created_at'] = str(datetime.now())

          item['source'] = "Gyn"

          yield item
