import scrapy

class GoogleSpider(scrapy.Spider):
	name="google"
	allowed_domains = ["google.co.in"]
	start_urls = [
	"https://www.google.co.in/?gfe_rd=cr&ei=asp0V_upD-rA8geEr5qgDA&gws_rd=ssl#q=modi"
	]
	def parse(self, response):
		

