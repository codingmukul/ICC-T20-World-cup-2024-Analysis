import scrapy

class team_logo_image(scrapy.Spider):
    name = 'logospider'
    start_urls = ['https://www.icc-cricket.com/tournaments/t20cricketworldcup/teams']

    def parse(self, response):
        image_links = response.css('.object-center::attr(src)').getall()
        country_names = response.css('.font-h1-upper::text').getall()
        for image, country in zip(image_links, country_names):
            yield {'Country':country, 'image':image}


