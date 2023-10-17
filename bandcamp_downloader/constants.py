import re
import os

COLLECTION_POST_URL = (
    "https://bandcamp.com/api/fancollection/1/collection_items"
)
FILENAME_REGEX = re.compile("filename\\*=UTF-8''(.*)")
WINDOWS_DRIVE_REGEX = re.compile(r"[a-zA-Z]:\\")
SANITIZE_PATH_WINDOWS_REGEX = re.compile(r'[<>:"/|?*\\]')
MAX_THREADS = 32
DEFAULT_THREADS = 5
DEFAULT_FILENAME_FORMAT = os.path.join("{artist}", "{artist} - {title}")
SUPPORTED_FILE_FORMATS = [
    "aac-hi",
    "aiff-lossless",
    "alac",
    "flac",
    "mp3-320",
    "mp3-v0",
    "vorbis",
    "wav",
]
SUPPORTED_BROWSERS = ["firefox", "chrome", "chromium", "brave", "opera", "edge"]
TRACK_INFO_KEYS = ["item_id", "artist", "title"]
