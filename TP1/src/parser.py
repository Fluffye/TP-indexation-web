from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def parse_html(html_content):
    return BeautifulSoup(html_content, "html.parser")


def extract_content(soup, base_url):
    # Title
    title = soup.title.string.strip() if soup.title else ""

    # First paragraph
    first_paragraph = ""
    p_tag = soup.find("p")
    if p_tag:
        first_paragraph = p_tag.get_text(strip=True)

    # internal links
    internal_links = []
    base_domain = urlparse(base_url).netloc

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(base_url, href)
        parsed_href = urlparse(full_url)

        if parsed_href.netloc == base_domain:
            internal_links.append({
                "url": full_url,
                "source": base_url
            })

    return {
        "url": base_url,
        "title": title,
        "first_paragraph": first_paragraph,
        "links": internal_links
    }
