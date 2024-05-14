from bs4 import BeautifulSoup
import requests
from pprint import pprint

# response = requests.get("https://news.ycombinator.com/")
# response.raise_for_status()
# yc_web_site = response.text

# soup = BeautifulSoup(yc_web_site, "html.parser")

# articles = [
#     {
#         "position": article.td.getText(), 
#         "title": article.select_one(".titleline a").getText(), 
#         "link": article.select_one(".titleline a").get("href")
#     }
#     for article in soup.select(".athing")
# ]

# scores = soup.select(".subline .score")
# scores = [int(score.getText().split(" ")[0]) for score in scores]
# # scores.sort()
# highest_score = max(scores)
# index = articles.index(highest_score)

# pprint(len(scores))

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

html_movies_data = response.text

soup = BeautifulSoup(html_movies_data, "html.parser")

articles = soup.select(".article-title-description__text")

articles_list = []
for article in articles:
    separator = ""
    if ")" in article.select_one(".title").getText():
        separator = ")"
    else:
        separator = (":")

    position = article.select_one(".title").getText().split(separator)[0]
    title = article.select_one(".title").getText().split(separator)[1]
    
    new_movie = {
        "position": position,
        "title": title
    }

    articles_list.append(new_movie)

articles_list.reverse()

with open("Day 40/movies.txt", encoding="utf-8", mode="w") as file:
    for article in articles_list:
        file.write(f"{article['position']}) {article['title']}\n")