# Export

## Export to Excel (openpyxl)

```shell
sudo pip install openpyxl
```

### code: `export_excel_demo`

```python
# -*- coding: utf-8 -*-
import scrapy, os, csv, glob
from openpyxl import Workbook

class ExportExcelDemoSpider(scrapy.Spider):
    name = 'export_excel_demo'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        yield {
            'H1 Tag': h1_tag,
            'Tags': tags
        }
    
    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)

        wb = Workbook()
        ws = wb.active

        with open(csv_file, 'r') as f:
            for row in csv.reader(f):
                ws.append(row)

        wb.save(csv_file.replace('.csv', '') + '.xlsx')

```

### To run

```shell
cd excel_export_demo
scrapy crawl export_excel_demo -o items.csv
```

Save data as `csv`, then convert csv to `xlsx(excel)`

