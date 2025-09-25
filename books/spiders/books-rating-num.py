import scrapy

class BooksRatingNumSpider(scrapy.Spider):
    name = "books_rating_num"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        rating_map = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }

        for product in response.css('article.product_pod'):
            title = product.css('h3 a::text').get()
            price = product.css('div.product_price p.price_color::text').get()
            rating_class = product.css('p.star-rating::attr(class)').get()
            rating_word = rating_class.split()[-1] if rating_class else None
            rating = rating_map.get(rating_word, 0)

            yield {
                'title': title,
                'price': price,
                'rating': rating  # Already numeric!
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
