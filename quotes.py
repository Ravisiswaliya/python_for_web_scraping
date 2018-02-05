'''
This script is for educational purpose only
'''

'''
I worte this script with the help of scrapy framework
This script can scrap whole blog post from blow given url
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['fonearena.com']
    start_urls = ['http://fonearena.com/blog/']

    def parse(self, response):
        #self.log('I just visited:' + response.url)
        for quote in response.css('article'):
            item = {
            'article' :quote.css("header.entry-header > h2.entry-title > a::text").extract_first(),
            "discription" :quote.css("div.entry-content > p::text").extract_first()

            }
            yield item

        #follow pagination
        i = response.css("div.nav-links>a.next::attr(href)").extract_first()
        i = response.urljoin(i)


        if i:

            yield scrapy.Request(url=i, callback=self.parse)
