from scrapy import Request
from scrapy.spiders import Spider
from arduinoProjects.items import ProjecthubItem

class ProjecthubSpider(Spider):
    name = 'projecthub'
    start_urls = ['https://create.arduino.cc/projecthub?category=internet-of-things-bt-wireless']

    def parse(self, response):
        item = ProjecthubItem()
        projects = response.xpath('//div[@class="thumb project-thumb"]//div[@class="thumb-inner"]')

        for project in projects:
            item['title'] = project.xpath('.//h4/span/a/text()').extract()[0]
            views = project.xpath('.//ul[contains(@class, "project-stats")]/li/span[@class="stat-figure"]/text()').extract()[0]
            item['views'] = int(views.replace(',', ''))
            respects = project.xpath('.//ul[contains(@class, "project-stats")]/li/span[@class="stat-figure"]/text()').extract()[1]
            item['respects'] = int(respects)

            yield item

        next_url = response.xpath('//ul[@class="pagination"]/li[contains(@class, "next")]/a/@href').extract()
        print(next_url)
        if next_url:
            next_url = 'https://create.arduino.cc' + next_url[0]
            yield Request(next_url)