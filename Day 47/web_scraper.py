import requests
from bs4 import BeautifulSoup

class PriceManager:
    def __init__(self) -> None:
        self.html = None
        self.soup = None


    def scrape_html_page(self, link:str):

        response = requests.get(
            url=link,
             headers={
                "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0"
            }
            # headers= {"User-Agent":"Defined"}
        )

        self.html = response.text
        self.soup = BeautifulSoup(self.html, "html.parser")

        print(self.soup)


    # def get_current_price(self, target_price: float):
    #     current_price: float

        