# Form Request

```python
from scrapy.http import FormRequest
data = {
    '__EVENTTARGET': "btnSearch",
    '__EVENTARGUMENT':"",
    '__VIEWSTATE': "/ wEPDwULLTIwNTMyMzMwMThkZLiCLeQCG/lBVJcNezUV/J0rsyMr",
    '__VIEWSTATEGENERATOR': "A7B2BBE2",
    'today': "20190810",
    'sortBy': "shareholding",
    'sortDirection': "desc",
    'alertMsg':"",
    'txtShareholdingDate': "2019/08/09",
    'txtStockCode': "00001",
    'txtStockName': "CK HUTCHISON HOLDINGS LIMITED",
    'txtParticipantID':"",
    'txtParticipantName':"",
    'txtSelPartID':"" }
# data came from browser:network:header:Form Data
page = FormRequest(url='https://www.hkexnews.hk/sdw/search/searchsdw.aspx', formdata=data)
fetch(page)
view(response)
```

