import scrapy
from ..items import potm

class playerdetails_spider(scrapy.Spider):
    name = 'matchdetails'
    start_urls = ['https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89']
    def parse(self, response):
        links = response.css('.ds-whitespace-nowrap+ .ds-text-right a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_link)

    def parse_link(self, response):
        item = potm(
            MatchId = response.css('.ds-leading-none+ .ds-text-typo .ds-block::text').get(),
            Name = response.css('tr:nth-child(5) .ds-ml-2::text').get(), 
            TossResult = response.css('tr:nth-child(2) .ds-font-regular::text').get()
        )
        yield item