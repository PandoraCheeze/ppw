import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "quote"

    def start_requests(self):
        csvdata = pd.read_csv('hasil_link.csv').values
        start_url = [ link[0] for link in csvdata ]

        for url in start_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'Judul': response.css('#content_journal > ul > li > div:nth-child(2) > a::text').get(),

            'Nama Penulis' : response.css('#content_journal > ul > li > div:nth-child(2) > div:nth-child(2) > span::text').get(),
            
            'Dosen Pembimbing I' : response.css('#content_journal > ul > li > div:nth-child(2) > div:nth-child(3) > span::text').get(),

            'Dosen Pembimbing II' : response.css('#content_journal > ul > li > div:nth-child(2) > div:nth-child(4) > span::text').get(),

            'Abstrak': response.css('#content_journal > ul > li > div:nth-child(4) > div:nth-child(2) > p::text').get()

        }

