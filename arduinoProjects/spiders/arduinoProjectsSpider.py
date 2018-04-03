import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from arduinoProjects.items import ArduinoProjectsItem
import urllib


class ArduinoProjects(CrawlSpider):
  name = 'arduinoProjects'
  start_urls = ['https://create.arduino.cc/projecthub']
  url = 'https://create.arduino.cc'

  def parse(self, response):
    item = ArduinoProjectsItem()
    selector = Selector(response)
    articles = selector.xpath('//div[@class="row thumb-list"]/div[@class="project-thumb-container"]')
    print(articles)

    for article in articles:
      title = article.xpath('div//div[@class="thumb-inner"]/h4/span/a/text()').extract()

      item['title'] = title

      yield item

    # next_link = selector.xpath('//ul[@class="pagination"]')