from bs4 import BeautifulSoup
import requests

movie_web_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url=movie_web_url)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
titles_list = [title.text for title in movie_titles]

titles_list.reverse()
print(titles_list)

with open('movies_list.txt', 'a') as f:
    for title in titles_list:
        f.write(f"{title}'\n'")