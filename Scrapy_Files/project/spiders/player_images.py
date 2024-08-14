import scrapy
from ..items import BowlingCard

class player_image(scrapy.Spider):
    name = 'imagespider'
    start_urls = ['https://www.icc-cricket.com/tournaments/t20cricketworldcup/teams']

    def parse(self, response):
        links = response.css('a[title="team profile"]::attr(href)').getall()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link, errback=self.errback_handle)

    def errback_handle(self, failure):
        self.logger.error(repr(failure))

    def parse_link(self, response):
        image_links = response.css('.ml-0 .swiper-wrapper img::attr(src)').getall()
        player_names = response.xpath('//*[@id="main"]/section[2]/div[1]/div[2]/div/div/div[1]/div/a/div/div[2]/div/div[1]/text()').getall()
        for image, name in zip(image_links, player_names):
            yield {'name':name, 'image':image}


