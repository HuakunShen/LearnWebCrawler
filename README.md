# Web Crawler Learning

## Login

Use web crawler to log into <http://quotes.toscrape.com/login>

```shell
cd login_spider
scrapy crawl login
```

After running the above command, a browser should show up, and it can be observed that in the top right corner, the `Login` button becomes `Logout` button, i.e. now it's logged in.



## Retrieve Data From <http://books.toscrape.com/>

There are 1000 books on this website, divided into 50 pages. This crawler go to each page, take url of each book, recursively go to each book's page and retrieve detailed information of that book. Then go on to the next book on the page.

After a page is down, get the url of next page button and go to next page and repeat the scraping process until all books are checked.

And flag `-o` to specify where to export the retrieved data.

```shell
cd books_crawler2
scrapy crawl booksData -o data.csv
```

Eventually a `data.csv` is generated. All information of every book are stored in the csv file. the csv file could be opened with excel for better displaying data.  

