import requests
from pyquery import PyQuery as pq
from urllib.parse import urljoin, urlparse

version_number = "5.1.9"

if __name__ == "__main__":
    home_url = "https://www.adobezii.com/universal-patcher/"
    
    response = requests.get(home_url)
    parsed_url = urlparse(home_url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc
    # doc = pq(response.text)
    # content_list = doc("")
    if 'Adobe Zii ' + version_number + ' CC2020 Universal Patcher' in response.text:
        print(version_number + " is realsed")
    else:
        print(version_number + " is not realsed")
