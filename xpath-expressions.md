下面的示例为http://example.com/
'''
$x('/html')
  [ <html>...</html> ]
$x('/html/body')
  [ <body>...</body> ]
$x('/html/body/div/p')
  [ <p>...</p>, <p>...</p> ]
$x('/html/body/div/p[1]')
  [ <p>...</p> ]
$x('//p')
  [ <p>...</p>, <p>...</p> ]
$x('//div//a')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a/@href')
  [ href="http://www.iana.org/domains/example" ]
$x('//a/text()')
  [ "More information..." ]
$x('//div/*')
  [ <h1>Example Domain</h1>, <p>...</p>, <p>...</p> ]
$x('//a[@href]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[@href="http://www.iana.org/domains/example"]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[contains(@href, "iana")]')
  [ <a href="http://www.iana.org/domains/example">More information...</a> ]
$x('//a[starts-with(@href, "http://www.")]')
  [ <a href="http://www.iana.org/domains/example">More information...</a>]
$x('//a[not(contains(@href, "abc"))]')
  [ <a href="http://www.iana.org/domains/example">More information...</a>]
```
以下是在scrapy中的应用，首先`scrapy shell http://example.com`
```python
response.xpath('/html').extract()
  [u'<html><head><title>...</body></html>']
response.xpath('/html/body/div/h1').extract()
  [u'<h1>Example Domain</h1>']
response.xpath('/html/body/div/p').extract()
  [u'<p>This domain ... permission.</p>', u'<p><a href="http://www.iana.org/domains/example">More information...</a></p>']
response.xpath('//html/head/title').extract()
  [u'<title>Example Domain</title>']
response.xpath('//a').extract()
  [u'<a href="http://www.iana.org/domains/example">More information...</a>']
response.xpath('//a/@href').extract()
  [u'http://www.iana.org/domains/example']
response.xpath('//a/text()').extract()
  [u'More information...']
response.xpath('//a[starts-with(@href, "http://www.")]').extract()
  [u'<a href="http://www.iana.org/domains/example">More information...</a>']
