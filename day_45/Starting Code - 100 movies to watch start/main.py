import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

titles = [title.get_text() + "\n" for title in soup.find_all("h3", class_="title")]

with open("movies.txt", "w") as file:
    file.writelines(titles[::-1])