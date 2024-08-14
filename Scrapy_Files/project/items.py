# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.link


class PlayerCard(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Country = scrapy.Field()
    Name = scrapy.Field()
    Role = scrapy.Field()
    Age = scrapy.Field()
    Batting = scrapy.Field()
    Bowling = scrapy.Field()
    Cap = scrapy.Field()

class BattingCard(scrapy.Item):
    MatchId = scrapy.Field()
    Country = scrapy.Field()
    Name = scrapy.Field()
    BattingOrder = scrapy.Field()
    OutMethod = scrapy.Field()
    Runs = scrapy.Field()
    Balls = scrapy.Field()
    Minutes = scrapy.Field()
    Fours = scrapy.Field()
    Sixes = scrapy.Field()
    SR = scrapy.Field()

class BowlingCard(scrapy.Item):
    MatchId = scrapy.Field()
    Country = scrapy.Field()
    Name = scrapy.Field()
    OversBowled = scrapy.Field()
    Maiden = scrapy.Field()
    Runs = scrapy.Field()
    Wickets = scrapy.Field()
    Economy = scrapy.Field()
    dots = scrapy.Field()
    fours = scrapy.Field()
    sixes = scrapy.Field()
    wides = scrapy.Field()
    noballs = scrapy.Field()

class potm(scrapy.Item):
    MatchId = scrapy.Field()
    Name = scrapy.Field()
    TossResult = scrapy.Field()
    
      
