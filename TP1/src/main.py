1

from config import MAX_PAGE, URL 
from extractor import crawl 
from storage import save_to_json

if __name__ == "__main__":
    start_url = "https://web-scraping.dev/products"
    data = crawl(start_url)
    save_to_json(data)