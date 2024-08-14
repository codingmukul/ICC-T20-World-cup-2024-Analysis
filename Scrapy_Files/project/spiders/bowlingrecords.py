import scrapy
from ..items import BowlingCard

class playerdetails_spider(scrapy.Spider):
    name = 'bowlingsummary'
    start_urls = ['https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89']

    def parse(self, response):
        links = response.css('.ds-whitespace-nowrap+ .ds-text-right a::attr(href)').getall()
        for link in links:

            full_link = "https://www.espncricinfo.com/" + link
            yield scrapy.Request(url=full_link, callback=self.parse_link, errback=self.errback_handle)

    def errback_handle(self, failure):
        self.logger.error(repr(failure))

    def parse_link(self, response):
        match_id = response.css('.ds-leading-none+ .ds-text-typo .ds-block::text').get()
        if not match_id:
            self.logger.error("Match ID not found on %s", response.url)
            return

        team_a_section = response.css('.incontent2 , .ds-mt-2:nth-child(2) .ds-mb-4 , .ds-mt-2:nth-child(2) .ds-bg-ui-fill-translucent-hover')
        if not team_a_section:
            self.logger.error("Team A section not found on %s", response.url)
            return

        team_a_name = team_a_section.css('.ds-capitalize .ds-capitalize::text').get()  
        team_b_section = response.css('.ds-mt-2+ .ds-mt-2 .ds-mb-4')
        team_b_name = team_b_section.css('.ds-capitalize .ds-capitalize::text').get()

        team_a_rows = team_a_section.css('tr')
        team_b_rows = team_b_section.css('tr')

        for row in team_a_rows:
            tds = row.css('td')
            if (len(tds) == 11 or len(tds) == 12):
                item = BowlingCard(
                    Name=row.css('.ds-block::text').get(),
                    Country=team_b_name,
                    MatchId=match_id,
                    OversBowled=row.css('.ds-text-right:nth-child(2)::text').get(),
                    Maiden=row.css('.ds-text-right:nth-child(3)::text').get(),
                    Runs=row.css('.ds-text-right:nth-child(4)::text').get(),
                    Wickets=row.css('strong::text').get(),
                    Economy=row.css('.ds-text-right:nth-child(6)::text').get(),
                    dots=row.css('.ds-text-right:nth-child(7)::text').get(),
                    fours=row.css('.ds-text-right:nth-child(8)::text').get(),
                    sixes=row.css('.ds-text-right:nth-child(9)::text').get(),
                    wides=row.css('.ds-text-right:nth-child(10)::text').get(),
                    noballs=row.css('.ds-text-right:nth-child(11)::text').get()
                )
                yield item

        for row in team_b_rows:
            tds = row.css('td')
            if (len(tds) == 11 or len(tds) == 12):
                item = BowlingCard(
                    Name=row.css('.ds-block::text').get(),
                    Country=team_a_name,
                    MatchId=match_id,
                    OversBowled=row.css('.ds-text-right:nth-child(2)::text').get(),
                    Maiden=row.css('.ds-text-right:nth-child(3)::text').get(),
                    Runs=row.css('.ds-text-right:nth-child(4)::text').get(),
                    Wickets=row.css('strong::text').get(),
                    Economy=row.css('.ds-text-right:nth-child(6)::text').get(),
                    dots=row.css('.ds-text-right:nth-child(7)::text').get(),
                    fours=row.css('.ds-text-right:nth-child(8)::text').get(),
                    sixes=row.css('.ds-text-right:nth-child(9)::text').get(),
                    wides=row.css('.ds-text-right:nth-child(10)::text').get(),
                    noballs=row.css('.ds-text-right:nth-child(11)::text').get()
                )
                yield item