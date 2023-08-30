import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        start_url = [
                'https://pta.trunojoyo.ac.id/c_search/byprod/7',
                'https://pta.trunojoyo.ac.id/c_search/byprod/7/2',
                'https://pta.trunojoyo.ac.id/c_search/byprod/7/3',
                ]
        for url in start_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('#content_journal > ul > li'):
            yield {
                'Link': item.css(f'div:nth-child(3) >  a::attr(href)').get(),
            }