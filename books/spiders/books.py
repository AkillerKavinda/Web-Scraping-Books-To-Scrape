import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

# First code
        # title = response.css('h3 a::text').extract()
        # price = response.css('div.product_price p.price_color::text').extract()
        # rating_class = response.css('p.star-rating::attr(class)').get()
        # rating = rating_class.split()[-1] if rating_class else None

# Looping code with rating for every item
        for product in response.css('article.product_pod'):
            title = product.css('h3 a::text').get()
            price = product.css('div.product_price p.price_color::text').get()
            rating_class = product.css('p.star-rating::attr(class)').get()
            rating = rating_class.split()[-1] if rating_class else None

            yield {
                'title': title,
                'price': price,
                # 'rating_class': rating_class,
                'rating': rating
            }

            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)