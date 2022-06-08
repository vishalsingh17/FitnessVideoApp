import youtube_dl
from youtube_dl.utils import DownloadError

ydl = youtube_dl.YoutubeDL()

def get_info(url):
    with ydl:
        results = ydl.extract_info()