# Web Crawler Learning

## Login

Use web crawler to log into <http://quotes.toscrape.com/login>

```shell
cd login_spider
scrapy crawl login
```

After running the above command, a browser should show up, and it can be observed that in the top right corner, the `Login` button becomes `Logout` button, i.e. now it's logged in.



## Retrieve Data From <http://books.toscrape.com/>, Part 1

There are 1000 books on this website, divided into 50 pages. This crawler go to each page, take url of each book, recursively go to each book's page and retrieve detailed information of that book. Then go on to the next book on the page.

After a page is explored, the crawler gets the url of `next page button`, go to next page and repeat the scraping process until all books are retrieved.

Add flag `-o` to specify where to export the retrieved data.

```shell
cd books_crawler2
scrapy crawl booksData -o data.csv
```

Eventually a `data.csv` is generated. All information of every book are stored in the csv file. the csv file could be opened with excel for better displaying data.  

## Retrieve Data From <http://books.toscrape.com/>, Part 2

```shell
cd books_crawler2
scrapy crawl booksData2 -a category="http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"
# the link is taken from books.toscrape.com by clicking one of the category.
```

When we only want to scrape books of one specific category, we can manually add `start_urls` in a OOP way.

```python
class Booksdata2Spider(Spider):
    name = 'booksData2'
    allowed_domains = ['books.toscrape.com']
	def __init__(self, category):
        self.start_urls = [category]
```

## Retrieve Data From <http://books.toscrape.com/>, Part 3, Close Function

* close function: function executed when scraping process is done

```shell
cd books_crawler2
scrapy crawl booksData2 -a category="http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html" -o items.csv
```

Regularly, the exported file will be saved as `items.csv`

With `close` function, it can be renamed.

```python
    import os, glob
    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file, 'newBooksItems.csv')
```



## Using `items.py`

