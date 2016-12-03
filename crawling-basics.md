下面的html片段
```
<strong class="ad-price txt-xlarge txt-emphasis" itemprop="price"> £334.39pw</strong>
```
尽量使用不包含视觉元素，即html标签的xpath表达式
```
>>> response.xpath('//*[@itemprop="price"][1]/text()').extract()
[u'\xa3334.39pw']
>>> response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
[u'334.39']
>>> response.css('.ad-price').xpath('text()')
[<Selector xpath='text()' data=u'\xa3334.39pw'>]
>>> response.css('.ad-price').xpath('text()').re('[.0-9]+')
[u'334.39']
```
示例，spider代码片段，基本爬虫, basic.py
```python
import scrapy
from properties.items import PropertiesItem

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = (
        'http://web:9312/properties/property_000000.html',
    )

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath(
            '//*[@itemprop="name"][1]/text()').extract()
        item['price'] = response.xpath(
            '//*[@itemprop="price"][1]/text()').re('[.0-9]+')
        item['description'] = response.xpath(
            '//*[@itemprop="description"][1]/text()').extract()
        item['address'] = response.xpath(
            '//*[@itemtype="http://schema.org/'
            'Place"][1]/text()').extract()
        item['image_urls'] = response.xpath(
            '//*[@itemprop="image"][1]/@src').extract()
        return item
```
保存输出到文件
```
$ scrapy crawl basic -o items.json
$ cat items.json
[{"price": ["334.39"], "address": ["Angel, London"], "description": ["website court ... offered"], "image_urls": ["../images/i01.jpg"], "title": ["set unique family well"]}]

$ scrapy crawl basic -o items.jl
$ cat items.jl
{"price": ["334.39"], "address": ["Angel, London"], "description": ["website court ... offered"], "image_urls": ["../images/i01.jpg"], "title": ["set unique family well"]}

$ scrapy crawl basic -o items.csv
$ cat items.csv 
description,title,url,price,spider,image_urls...
"...offered",set unique family well,,334.39,,../images/i01.jpg

$ scrapy crawl basic -o items.xml
$ cat items.xml 
<?xml version="1.0" encoding="utf-8"?>
<items><item><price><value>334.39</value></price>...</item></items>
```
上传输出到FTP或S3 bucket
```
$ scrapy crawl basic -o "ftp://user:pass@ftp.scrapybook.com/items.json "
$ scrapy crawl basic -o "s3://aws_key:aws_secret@scrapybook/items.json"
```
代码片段，爬取列表，产品页面，手动提供url
```python
def parse(self, response):
    # Get the next index URLs and yield Requests
    next_selector = response.xpath('//*[contains(@class,'
                                   '"next")]//@href')
    for url in next_selector.extract():
        yield Request(urlparse.urljoin(response.url, url))

    # Get item URLs and yield Requests
    item_selector = response.xpath('//*[@itemprop="url"]/@href')
    for url in item_selector.extract():
        yield Request(urlparse.urljoin(response.url, url),
                      callback=self.parse_item)
```
用crawl spider爬取列表，产品页面
```python
...
class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    start_urls = ['http://www.web/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'),
         callback='parse_item')),
    )

    def parse_item(self, response):
        ...
```
