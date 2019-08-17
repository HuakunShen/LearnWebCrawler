# Web Crawler Learning

## Login

Use web crawler to log into <http://quotes.toscrape.com/login>

```shell
cd login_spider
scrapy crawl login
```

After running the above command, a browser should show up, and it can be observed that in the top right corner, the `Login` button becomes `Logout` button, i.e. now it's logged in.

## Selenium search Google with robot

* make sure `selenium` is installed to current `python`
* make sure `ChromeDriver` is downloaded and palced into a directory under path variable.

```shell
cd seleniumDemo
python searchGoogle.py
```

## Download 2000 chapters of novel
* Navigate to `download_novel` directory. There are two versions of code that do the same job.
  One use iteration and the other uses recursion. Personally, I believe iteration saves more memory. 


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

```shell
cd sample_items_spider
scrapy crawl sample_items_spider
```

The code above retrieves authors' names from `quotes.toscrape.com`.

Instead of using `yield` as I do previously, I use `items.py` instead.

## Export Excel

For details, see `./Note/Lec7_Export`

```shell
cd excel_export_demo
scrapy crawl export_excel_demo -o items.csv
```

Save data as `csv`, then convert csv to `xlsx(excel)`

## Download Image

See `./download_image/README.md` for details

```shell
cd download_image
sudo scrapy crawl books > ./log.txt
```

Images will be stored in `./download_image/books_crawler/books_crawler/downloaded_images`

Check `log.txt` for exact location.

## Store Data in Database

Details see **Lec9** in Notes

* SQL:

  * ```shell
    cd books_crawler2
    scrapy crawl booksData4_SQL -o items.csv > log.txt
    ```

  * Make sure `mysql-server` is installed locally and service is started.

  * Data will be stored in mySQL database 

* MongoDB

  * ```shell
    cd booksCrawler_MongoDB
    scrapy crawl booksData4_SQL -o items.csv > log.txt
    ```

  * Make sure `mongod` service is started locally

  * Data will be stored in MongoDB

## Scrapy User Agent

```shell
scrapy shell 'https://www.amazon.ca/gp/profile/amzn1.account.AERSRZ2IKWWLCTLHRZKEW4SXX23Q/ref=cm_cr_arp_d_gw_rgt?ie=UTF8'
# the above won't give a valid response, try 
view(response)		# this page will be blank
```

Go to `<https://www.whatismybrowser.com/detect/what-is-my-user-agent>` , to find out your user agent.

```shell
scrapy shell 'https://www.amazon.ca/gp/profile/amzn1.account.AERSRZ2IKWWLCTLHRZKEW4SXX23Q/ref=cm_cr_arp_d_gw_rgt?ie=UTF8' -s USER_AGENT="paste user agent here" # -s stands for setting
```

## Scrape Tables

scrape a table from `<https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population>`

```shell
cd scrapeTable
scrapy crawl wiki -o output.json
```

## Scrape JSON

```shell
cd scrapeJSON
scrapy crawl tweets -o output.csv
# EASY
```

