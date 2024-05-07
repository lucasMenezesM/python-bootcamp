import requests
from dotenv import dotenv_values
from IndividualNews import IndividualNews

config = dotenv_values("Day 36/.env")
COMPANY_NAME = "Tesla"
STOCK = "TSLA"

class NewsList:
    def __init__(self) -> None:
        self.news_list: list[IndividualNews] = []

    def save_news(self, quantity: int) -> None:
        response = requests.get(
        url=config["NEWS_API_ENDPOINT"],
        params={
            "q":COMPANY_NAME, 
            "apiKey":config["NEWS_API_KEY"]
        })

        response.raise_for_status()
        data = response.json()["articles"]
        # print(data["articles"])
        # print("News data")

        for index, news in enumerate(range(quantity)):
            if index > quantity:
                break
            
            if "[Removed]" in data[index]["description"] or "[Removed]" in data[index]["title"]:
                continue

            news = IndividualNews(
                source= data[index]["source"]["name"],
                author=data[index]["author"],
                title=data[index]["title"],
                description=data[index]["description"],
                url=data[index]["url"],
                publication=data[index]["publishedAt"]
            )
            
            self.news_list.append(news)
        return news
    

    def get_news(self) -> list[IndividualNews]:
        if len(self.news_list) == 0:
            print("News list is empty")
        else:
            return self.news_list
    