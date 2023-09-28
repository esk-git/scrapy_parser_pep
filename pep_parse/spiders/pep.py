import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_urls_peps = response.css('a[href^="pep-"]')
        for pep_link in all_urls_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ', 1)
        )
        data = {
            'number': number.split()[1],
            'name': name,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
