import time
import urllib.request
from urllib.error import URLError, HTTPError
import urllib.robotparser as robotparser
from urllib.parse import urlparse
from config import USER_AGENT, REQUEST_DELAY

def fetch_url(url, timeout=10):
    headers = {
        "User-Agent": USER_AGENT
    }
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.error.urlopen(request, timeout=timeout) as response:
            if response.status == 200:
                return response.read()
    except HTTPError as e:
        print(f"HTTP error {e.code} for {url}")
    except URLError as e:
        print(f"URL error for {url}: {e.reason}")

    return None


def can_fetch(url, user_agent= USER_AGENT):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()

    return rp.can_fetch(user_agent, url)


def get_page(url):
    if not can_fetch(url):
        print(f"Blocked by robots.txt: {url}")
        return None
    time.sleep(REQUEST_DELAY)
    return fetch_url(url)
