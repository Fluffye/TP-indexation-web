import heapq
import json
import time
from urllib.request import urlopen, Request
from request_http import can_fetch, get_page
from parser import parse_html, extract_content

def get_priority(url):
    if "product" in url.lower():
        return 0  # high priority
    return 1      # medium priority

def crawl(start_url):
    visited = set()
    queue = []
    results = []

    max_pages = 50

    # add the starting URL
    heapq.heappush(queue, (get_priority(start_url), start_url))

    while queue and len(visited) < max_pages:
        priority, url = heapq.heappop(queue)

        if url in visited:
            continue

        # respect of robots.txt
        if not can_fetch(url):
            continue

        print(f"Crawling ({len(visited)+1}/50) :", url)
        visited.add(url)

        try:
            request = Request(url, headers={"User-Agent": "MyCrawler"})
            response = urlopen(request, timeout=10)
            html = response.read()
        except Exception as e:
            print("Erreur :", e)
            continue

        soup = parse_html(html)
        page_data = extract_content(soup, url)
        results.append(page_data)

        # add new links to the file
        for link in page_data["links"]:
            link_url = link["url"]
            if link_url not in visited:
                heapq.heappush(queue, (get_priority(link_url), link_url))

        # politness
        time.sleep(1)

    return results





