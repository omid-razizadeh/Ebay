# Ebay
DP

There are different ways to extract information from webpages:

1.Computer vision

2.Using regular expressions

3.Web scraping like beautifulsoup or crawlers in python

We choose the third one and we want to extract some information from amazon and ebay website.

For this we need to know a little bit of css or xpath and the structure of scrapy library in python.

**In xpath:**

@ represents "attribute"
examples:
@class

@id

@href

Some examples:

**Xpath and CSS equivalency:**

xpath = '/html/body//div/p[2]'

css = 'html > body div > p:nth-of-type(2)'


Now, We can jump a little bit in more details:

::attr(attr-name)

css_locator = 'div#uid > a::attr(href)'

**Text extraction(::text)**

Example:

Hello world!

sel.css('p#p-example::text').extract()

Now for Scraping we need to know one more thing response:

product_name = response.css('h3.s-item__title::text').extract()

**In my project, I wanted to extract information of product name and product price. I extracted the information by something like this:**

```python
        product_name = response.css('h3.s-item__title::text').extract()
        product_price1 = response.css('.s-item__price::text').extract()
```

Then after scraping, I needed to post-process my data as It had some syntax. To remove it I used regular expressions:

```python
product_price = [re.sub('\xa0', '', fname) for fname in product_price1]
```

**Structure of scrapy:**

We need to first name the class and then define parse function and finally by using response extract the desired information.

```python
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 3
    start_urls = [
        'https://ru.ebay.com/b/Iced-Teas/38181/bn_7115588208'
    ]
```

**Note1.:For some websites like amazon they block to scrape. To overcome this difficulty there are some ways. I used proxy in my project.**

another common way is user-agent. I used scrapy-proxy-pool tool and I just paste this syntax in settings of my scrapy:

```
DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
```

More information about how to set up proxy in your scrapy projects can be found on some github pages like:

https://github.com/hyan15/scrapy-proxy-pool

**Pagination:**
Another problem in web scraping is that our scrapy be able to go to next pages and scrape next page information as well. 
We can do this by defining something like this:
```python
next_page = 'https://ru.ebay.com/b/Iced-Teas/38181/bn_7115588208?_pgn='+ str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <= 8:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
```
