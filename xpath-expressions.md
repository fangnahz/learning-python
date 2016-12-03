下面的示例为http://example.com/
```
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
以下是在scrapy中的应用，首先`scrapy shell http://example.com`，
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
```
取得包含id 'firstHeading'的div之内span部分的text文本
`//div[@id="firstHeading"]/span/text()`
取得包含id 'toc'的div之内ul之下所包含的所有a标签内的url
`//div[@id="toc"]/ul//a/@href`
对于所有有class属性，并且属性中含有“ltr”和“skin-vector”的元素，取得其内所有h1头元素的文本
`//*[contains(@class,"ltr") and contains(@class,"skin-vector")]//h1//text()`
取得含有class属性，属性值为“infobox”的table元素内第一个图片的url
`//table[@class="infobox"]//img[1]/@src`
取得含有class属性，属性值以“reflist”开头的div元素内所有a元素属性内的url链接
`//div[starts-with(@class,"reflist")]//a/@href`
如果某元素的子元素文本内容含有“References”，取得在该元素随后元素的a标签内容（链接）
注意，由于这个xpath表达式对html内容作出很多假设，所以容易失效。
`//*[text()="References"]/../following-sibling::div//a`
取得页面内所有图片的url
`//img/@src`
