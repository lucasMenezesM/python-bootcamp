import requests
from bs4 import BeautifulSoup
from pprint import pprint

class MusicScraper:
    def __init__(self) -> None:
        self.music_list = []

    
    def scrape_musics_by_year(self, year:str) -> None:
        url = f"https://www.billboard.com/charts/hot-100/{year}-08-12/"
        response = requests.get(url=url)
        response.raise_for_status()
        html_website = response.text

        soup = BeautifulSoup(html_website, "html.parser")
        
        # titles_from_html = soup.find_all(name="h3", class_="c-title")
        titles_from_html = soup.select(selector="li h3", class_="c-title")
        titles = [title.getText().replace("\n", " ").replace("\t", " ").strip() for title in titles_from_html]
        titles = titles[:100]
        self.music_list = titles