# Download Image With Pillow

```shell
sudo pip install Pillow
```

Uncomment ITEM_PIPELINES in `setting.py`
Replace with the following,
```python
import os
cur_working_dir = os.getcwd()
ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'books_crawler.pipelines.BooksCrawlerPipeline': 2
}
dir_path = os.path.dirname(os.path.realpath(__file__))
addr = os.path.join(dir_path, 'downloaded_images')
IMAGES_STORE = addr
print("debug: images stored in \n", IMAGES_STORE)
```
## To Run
```shell
sudo scrapy crawl books > ./log.txt
```
In log.txt you can check where the images are stored in case you cannot find them.
`'books_crawler.pipelines.BooksCrawlerPipeline': 2` is for renaming purpose. See `pipeline.py` for code.

