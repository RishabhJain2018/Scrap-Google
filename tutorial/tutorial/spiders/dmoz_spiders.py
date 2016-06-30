import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains = ["www.dmoz.org"]
	start_urls = [
	"http://doc.scrapy.org/en/latest/_static/selectors-sample1.html"	]

	def parse(self, response):
		for sel in response.xpath('//a'):
			item = DmozItem()
			item['title'] =sel.xpath('text()').extract()
			item['link'] = sel.xpath('@href').extract()
			# item['desc'] = sel.xpath('text()').extract()
			yield item



