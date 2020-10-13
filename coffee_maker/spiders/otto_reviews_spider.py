import scrapy
import json
from pprint import pprint


class OttoReviewsSpider(scrapy.Spider):
    name = "otto_reviews"

    start_urls = [
        'https://www.otto.de/product-customerreview/reviews/presentation/product/898416526'
    ]

    def parse(self, response):
        result = json.loads(response.body)
        for review in result['items']:
            data = review['data']
            yield {
                'title': data['title'],
                'text': data['text'],
                'rating': data['rating'],
                'creationDate': data['creationDate']
            }