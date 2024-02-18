from bs4 import BeautifulSoup
import requests
import os

def dl_panda(url):
    html = requests.get("https://dlpanda.com", params={"url":url, "token":"G7eRpMaa"}).text
    soup = BeautifulSoup(html, 'html.parser')
    video_tag = soup.find("video")
    if video_tag:
        source_tag = video_tag.find("source")
        file_url = source_tag.get('src')
        if not any(scheme in file_url for scheme in ["http://", "https://"]):
            file_url = "http:" + source_tag.get('src')
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