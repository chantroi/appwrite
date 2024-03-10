from bs4 import BeautifulSoup
import requests
import os

UA = "Mozilla/5.0 (Linux; Android 13; M2102J20SG Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.66 Mobile Safari/537.36"

def dl_panda(url):
    html = requests.get("https://dlpanda.com", params={"url":url, "token":"G7eRpMaa"}, headers={"User-Agent": UA}).text
    soup = BeautifulSoup(html, 'html.parser')
    video_tag = soup.find("video")
    if video_tag:
        source_tag = video_tag.find("source")
        file_url = source_tag.get('src')
        if not file_url.startswith("http"):
            file_url = "https:{}".format(file_url)
        is_video = True
    else:
        imgtags = soup.find_all('img', style="max-width: none; max-height: none;")
        file_url = [itag.get("src") for itag in imgtags]
        is_video = False
    return file_url, is_video

def main(context):
    url = context.req.query.get('url')
    if url:
        file_url, is_video = dl_panda(url)
        return context.res.json({"url":file_url, "is_video":is_video})
    else:
        return context.res.send("No URL found", 400, {"content-type":"text/plain"})