from web_scraper import PriceManager
from bs4 import BeautifulSoup
import requests
from pprint import pprint

# price_manager = PriceManager()
# price_manager.scrape_html_page(link="https://keepa.com/#!product/12-6555526394")

response = requests.get(
    url="https://camelcamelcamel.com/product/6555522879",
    headers={
        "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "User-Agent": "Defined"
    }
)
html_data = response.text
# print(html_data)
soup = BeautifulSoup(html_data, "html.parser")
price = soup.select(".subheader")
print(html_data)