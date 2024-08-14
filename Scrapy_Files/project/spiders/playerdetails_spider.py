import scrapy
from ..items import PlayerCard

class playerdetails_spider(scrapy.Spider):
    name = 'playerdetails'
    start_urls = ['https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/squads']

    def parse(self, response):

        links = response.css('.ds-space-x-2 a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_link)

    def parse_link(self, response):
        country = response.css('.ds-mb-4 .ds-border-line .ds-border-line .ds-capitalize::text').getall()  
        players = response.css('.ds-p-3')
        for player in players:
            item = PlayerCard()
            item['Country'] = country
            item['Name'] = player.css('.ds-cursor-pointer::text').getall()
            item['Role'] = player.css('.ds-mt-1::text').getall()
            item['Cap'] = player.css('.ds-font-medium::text').getall()
            item['Age'] = player.css('.ds-items-center .ds-text-compact-xxs.ds-font-bold::text').getall()
            item['Batting']=player.css('.ds-items-center+ .ds-space-x-1 .ds-font-bold::text').getall()
            item['Bowling']=player.css('.ds-items-start+ .ds-space-x-1 .ds-font-bold::text').getall()
            yield item

