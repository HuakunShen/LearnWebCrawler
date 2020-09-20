# Download blob Media

> BLOB: Binary Large Object

When looking for video links within dev tool, the url that starts with `blob:` does lead you to the correct source of video, and the URL is actually different everytime you refresh the browser.

The URL is actually a memory address of the server which hosts the media.



## Download Video

1. Open Dev Tool of browser, go to **network**, filter by **m3u8**

2. Download video with the request URL with **ffmpeg**, URL may be in the m3u8 file too.

    ```bash
    ffmpeg -i "https://www.example.com/video/xxx" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 video_name.mp4
    ```

### Python Sample Code

```python
#!/usr/bin/env python3
import os
import subprocess
import requests,urllib
from bs4 import BeautifulSoup

pwd = os.path.split(os.path.realpath(__file__))[0]

url = "https://www.topgear.com/videos"

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'cookie': "cookie-placeholder",
    'cache-control': "no-cache"}

if __name__ == '__main__':
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    videoId = soup.find_all('video', class_="video-js")[0]['data-video-id'] ##获取视频Id
    title = soup.find_all('h1', class_="video-player__title")[0].contents[0] ##获取视频标题
    url = "https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId={}&secure=true".format(videoId)  ##生成视频下载Url
    filename = '{}.mp4'.format(title).replace(" ","-")
    cmd_str = 'ffmpeg -i \"' + url + '\" ' + '-acodec copy -vcodec copy -absf aac_adtstoasc ' + pwd + "/" +filename  ##下载视频
    print(cmd_str)
    subprocess.call(cmd_str,shell=True)

```





## Reference

### Video

[What is a blob URI?](https://www.youtube.com/watch?v=UgCCR-ZBP8w&t=8s&ab_channel=SynaptikLabs)

[What is a Data URI and how do I use it?](https://www.youtube.com/watch?v=dUhP4JWgwdo&ab_channel=SynaptikLabs)

[(Python基础教程之二十二)爬虫下载网页视频(video blob)](https://blog.csdn.net/novelly/article/details/106272012)

