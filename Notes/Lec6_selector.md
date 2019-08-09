# Selector

## xpath

```python
response.xpath('//*')		# select all
response.xpath('//*[@attribute="value"]')	# select all elements with attribute = "value"
response.xpath('//*[@attribute="value"/text()]')	# get text of elements selected above
response.xpath('//*[@attribute="value"/text()]').extract() # extract text to a list


```

## css

