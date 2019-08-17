import requests
from pyquery import PyQuery as pq
from urllib.parse import urljoin, urlparse


def parse_page(count, url, title):
    r = requests.get(url)
    r.encoding = 'GBK'
    page = pq(r.text)
    content = page('#content')
    text = content.text()
    filename = "./chapters/{0}. {1}.txt".format(str(count), title)
    with open(filename, 'w') as f:
        f.write(title + '\n\n\n')
        f.write(text)


if __name__ == "__main__":
    home_url = "https://www.yangguiweihuo.com/1/1680/"
    file_count = 0
    response = requests.get(home_url)
    parsed_url = urlparse(home_url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc
    response.encoding = 'GBK'
    doc = pq(response.text)
    print("开始下载")
    content_list = doc(".listmain a")
    for item in content_list.items():
        print("正在下载: ", item.text())
        page_url = urljoin(base_url, item.attr('href'))
        parse_page(file_count, page_url, item.text())
        file_count += 1
