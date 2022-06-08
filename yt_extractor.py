import youtube_dl
from youtube_dl.utils import DownloadError

ydl = youtube_dl.YoutubeDL()

def get_info(url):
    with ydl:
        try:
            result = ydl.extract_info(url, download=False)
        except DownloadError:
            return None

    if "entries" in result:
        video = result['entries'][0]
    
