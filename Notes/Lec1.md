# Lec1

```python
# http://quotes.toscrape.com/
fetch("http://quotes.toscrape.com/")		# then response is defined
# css selector
response.css('h1')
# xpath selector
response.xpath('//h1')		# select h1 tag
response.xpath('//h1/a')	# select a tag inside h1 tag
response.xpath('//h1/a/text()')	# select text inside h1/a
response.xpath('//h1/a/text()').extract()	# select only text
response.xpath('//h1/a/text()').extract_first()	# select only text

# select by class
response.xpath('//*[@class="tag-item"]')	# return a list of objects selected
response.xpath('//*[@class="tag-item"]/a')
response.xpath('//*[@class="tag-item"]/a/text()')
response.xpath('//*[@class="tag-item"]/a/text()').extract()


# export data
scrapy crawl quotes -o items.csv
scrapy crawl quotes -o items.json
scrapy crawl quotes -o items.xml
```

