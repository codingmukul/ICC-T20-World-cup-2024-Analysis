import scrapy

class matchlist_spider(scrapy.Spider):
    name = 'matchlist'
    start_urls = ['https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89']

    def parse(self, response):

        rows = response.css('tr')
        headers = rows[0].css('span::text').getall()
        for row in rows[1:]:
            # Extract each cell's data within the row
            cells = row.css('span::text').getall()

            # Zip headers with the corresponding row data
            if len(cells) == len(headers):
                row_data = dict(zip(headers, cells))
                yield row_data
        