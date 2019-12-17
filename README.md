# ebay12
DP

There are different ways to extract information from webpages:

    Computer vision

    Using regular expressions

    Web scraping like beautifulsoup or crawlers in python

    We choose the third one and we want to extract some information from amazon and ebay website.

    For this we need to know a little bit of css or xpath and the structure of scrapy library in python.

    In xpath:

    @ represents "attribute"

    examples:

    @class

    @id

    @href

    Some examples:

Xpath and CSS equivalency:

xpath = '/html/body//div/p[2]'

css = 'html > body div > p:nth-of-type(2)'

Now, We can jump a little bit in more details:

::attr(attr-name)

css_locator = 'div#uid > a::attr(href)'

Text extraction(::text)

Example:

Hello world!

sel.css('p#p-example::text').extract()

Now for Scraping we need to know one more thing response:

product_name = response.css('h3.s-item__title::text').extract()

Structure of scrapy:

We need to first name the class and then define parse function and finally by using response extract the desired information.

Note:For some websites like amazon they block to scrape. To overcome this difficulty there are some ways. I used proxy in my project.

More information about how to set up proxy in your scrapy projects can be found on some github pages like:

https://github.com/hyan15/scrapy-proxy-pool
