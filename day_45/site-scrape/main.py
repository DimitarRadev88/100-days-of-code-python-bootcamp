import requests
from bs4 import BeautifulSoup

live_response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(live_response.content, "html.parser")

# static_response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
# soup = BeautifulSoup(static_response.content, "html.parser")

def find_the_highest_scored_article():
    rows = soup.find_all("span", class_="score")
    highest_score = -1
    highest_score_id = None

    for row in rows:
        current_score = int(row.text.split(" ")[0])
        if current_score > highest_score:
            highest_score = current_score
            highest_score_id = row.get("id")

    article = soup.find(id=highest_score_id.replace("score_", "")).select_one("span.titleline>a")

    return {
        "title": article.get_text(),
        "link": article.get("href"),
        "score": highest_score
    }

# def get_articles_data():
#     articles = soup.select("span.titleline>a")
#     print(len(articles))
#     scores = soup.find_all("span", class_="score")
#     print(len(scores))
#
#     articles_list = []
#
#     for n in range(0, len(articles)):
#         article_info = {
#             "title": articles[n].get_text(),
#             "link": articles[n].get("href"),
#             "score": scores[n].get_text(),
#         }
#
#         articles_list.append(article_info)
#
#     return articles_list
#
# def sort_fun(d):
#     return d["score"]
#
# articles_info = get_articles_data()
#
# articles_info.sort(key=sort_fun, reverse=True)
#
# highest_scored_article = articles_info[0]
# print(highest_scored_article["title"])
# print(highest_scored_article["link"])
# print(highest_scored_article["score"])

highest_scored_artice = find_the_highest_scored_article()
print(highest_scored_artice["title"])
print(highest_scored_artice["link"])
print(highest_scored_artice["score"])
