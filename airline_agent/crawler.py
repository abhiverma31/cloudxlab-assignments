import re
import time
import os
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
import html2text

# ---- config ----
BASE_DOMAIN = "www.emirates.com"
HELP_SITEMAP = "https://www.emirates.com/english/help/sitemap-help-1.xml"
SCOPE_PREFIX = "/english/help/"    # only crawl pages under this path
OUT_DIR = "kb"                      # where .md files get saved
CRAWL_DELAY = 3                     # seconds between requests (polite default;
                                    # their robots.txt doesn't set a Crawl-Delay)
USER_AGENT = "Mozilla/5.0 (compatible; research-crawler/1.0)"

# only keep pages whose path mentions one of these support topics
TOPIC_KEYWORDS = [
    "baggage", "refund", "cancel", "special-assistance", "assistance",
    "infant", "child", "disab", "wheelchair", "pet", "unaccompanied-minor",
    "medical", "visa", "health", "delay", "damaged", "prohibited",
    "excess", "lost-property", "faq",
]

# paths their robots.txt explicitly disallows (checked before fetching)
DISALLOWED = [
    "/SessionHandler.aspx", "/TealeafTarget.aspx", "/sessionhandler.aspx",
    "/tealeaftarget.aspx", "/sessionkeepalive.aspx", "ExternalTransfer.aspx",
    "/WebResource.axd", "/resources", "/pop-ups/", "/mail-to-friend.aspx",
    "/mailtofriend.aspx", "/certificate-request/", "/destinations/city.aspx",
    "/destinations/airport.aspx", "/experience/login/", "/ekgroup/id",
    "flightstatus-results.aspx", "/woyf/", "find-visa-requirements",
    "/sso/login-redirect", "/service/dex/request-handler", "/booking/",
]

os.makedirs(OUT_DIR, exist_ok=True)

md_converter = html2text.HTML2Text()
md_converter.ignore_links = False
md_converter.body_width = 0  # don't hard-wrap lines


def should_follow(url: str) -> bool:
    """Can we queue this link at all? Broad check - stay under the
    help hub and away from disallowed paths. Deliberately does NOT filter
    by topic keyword, so category/nav pages can still be crawled through
    to reach topic pages linked beneath them."""
    parsed = urlparse(url)
    if parsed.netloc != BASE_DOMAIN:
        return False
    if not parsed.path.startswith(SCOPE_PREFIX):
        return False
    if any(bad in parsed.path for bad in DISALLOWED):
        return False
    return True


def should_save(url: str) -> bool:
    """Should this specific page's content be written out as a .md file?
    Narrower check - only pages whose URL mentions one of our support
    topics, so nav/index pages don't clutter the kb."""
    parsed = urlparse(url)
    return any(kw in parsed.path.lower() for kw in TOPIC_KEYWORDS)


def url_to_filename(url: str) -> str:
    path = urlparse(url).path.strip("/")
    safe = path.replace("/", "_") or "index"
    return os.path.join(OUT_DIR, f"{safe}.md")


def fetch_sitemap_urls(sitemap_url: str) -> list:
    resp = requests.get(sitemap_url, headers={"User-Agent": USER_AGENT}, timeout=15)
    resp.raise_for_status()
    return re.findall(r"<loc>(.*?)</loc>", resp.text)


# seed the queue from every URL in the help sitemap that matches our topics -
# this replaces blind link-following as the starting point, since Emirates'
# sitemap already enumerates real content pages directly
seed_urls = [u for u in fetch_sitemap_urls(HELP_SITEMAP) if should_follow(u)]
print(f"Seeded {len(seed_urls)} URLs from {HELP_SITEMAP}")

visited = set()
queue = list(seed_urls)

while queue:
    url = queue.pop(0)
    if url in visited:
        continue
    visited.add(url)

    print(f"Fetching: {url}")
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
    except requests.RequestException as e:
        print(f"  failed: {e}")
        continue

    if resp.status_code != 200:
        print(f"  skipped, status {resp.status_code}")
        time.sleep(CRAWL_DELAY)
        continue

    soup = BeautifulSoup(resp.text, "html.parser")

    if should_save(url):
        # try to isolate main content, fall back to full body
        main = soup.find("main") or soup.body
        title = soup.title.string.strip() if soup.title else url

        markdown = md_converter.handle(str(main))
        frontmatter = f"---\nurl: {url}\ntitle: {title}\n---\n\n"

        out_path = url_to_filename(url)
        with open(out_path, "w") as f:
            f.write(frontmatter + markdown)
        print(f"  saved -> {out_path}")
    else:
        print("  not a topic page, not saved (still checking its links)")

    # discover new links from this page - follow broadly, save selectively
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"]).split("#")[0]  # drop anchors
        if should_follow(link) and link not in visited:
            queue.append(link)

    time.sleep(CRAWL_DELAY)

print(f"Done. Crawled {len(visited)} pages into '{OUT_DIR}/'.")
