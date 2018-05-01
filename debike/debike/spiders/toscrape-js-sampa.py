import scrapy
from debike.items import Station

from datetime import datetime

class ToScrapeJsSampa(scrapy.Spider):
    name = 'toscrape-js-sampa'
    start_urls = ['https://bikesampa.tembici.com.br/bikesampa/mapaestacao.asp']

    def parse(self, response):

        # Parse <script>
        data = response.xpath('//script').re('exibirEstacaMapa\(\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\",\r\n\"(.*)\"')
  
        # Total Stations Data/SizeOfArrayAttr
        stations = int(len(data)/10)

        for i in range(0, stations):
          item = Station()

          k = i*10
          s = [data[0+k],data[1+k],data[2+k],data[3+k],data[4+k],
                data[5+k],data[6+k],data[7+k],data[8+k], data[9+k]]

          # ['latitude, longitude, icone, Nome, IdEstacao, StatusOnline, StatusOperacao, VagasOcupadas, numBicicletas, Endereco']          
          item['lat']     = float(s[0])
          item['lng']     = float(s[1])
          item['name']    = s[3]
          item['status']  = s[5]

          item['available'] = int(s[7])
          item['free']    = int(s[8])-int(s[7])
          item['address'] = s[9]
          item['created_at'] = str(datetime.now())

          item['source'] = 'sampa'

          yield item