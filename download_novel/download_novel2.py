import requests
from pyquery import PyQuery as pq
from urllib.parse import urljoin, urlparse


def parse_page(count, url, base_url):
    r = requests.get(url)
    r.encoding = 'GBK'
    page = pq(r.text)
    content = page('#content')
    title = page("h1").text()
    text = content.text()
    print("正在下载: ", title)
    # write to file
    filename = "./chapters2/{0}. {1}.txt".format(str(count), title)
    with open(filename, 'w') as f:
        f.write(title + '\n\n\n')
        f.write(text)
    # Go to next page
    next_page_btn = page('a:contains("下一章")')
    next_page_url = urljoin(base_url, next_page_btn.attr("href"))
    parse_page(count + 1, next_page_url, base_url)


if __name__ == "__main__":
    print("开始下载")
    start_url = "https://www.yangguiweihuo.com/1/1680/749491.html"
    parsed_url = urlparse(start_url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc
    parse_page(1, start_url, base_url)
