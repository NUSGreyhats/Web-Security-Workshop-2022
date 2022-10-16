from selenium import webdriver
from constants import COOKIE
import multiprocessing
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

def visit(base_url: str, link: str) -> str:
    """Visit the website"""
    p = multiprocessing.Process(target=_visit, args=(base_url, link))
    p.daemon = True
    p.start()
    return f"Visiting {link}"


def _visit(base_url: str, link: str) -> str:
    """Visit the website"""
    with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
        try:
            driver.get(base_url)
            cookie = {"name": "flag", "value": COOKIE["flag"]}
            driver.add_cookie(cookie)
            driver.get(base_url)
            driver.get(link)
            print(f"Visited {link}")
        except Exception as e:
            print(f"Connection Error: {link}\n{e}")
