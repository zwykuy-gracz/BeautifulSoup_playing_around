from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

article_title = soup.find(name='tr', class_='athing')
anchor_tag = article_title.find(name='a', id='')
link = anchor_tag.get('href')
# print(link)

score_list = []
all_article_info = soup.find_all(name='span', class_="score")
for i, art in enumerate(all_article_info):
    score = int(art.getText().split()[0])
    score_list.append(score)

highest_score = max(score_list)
print(highest_score)

for substring in all_article_info:
    if substring.getText().startswith(str(highest_score)+" "):
        highscore_id = substring.get('id').split('_')[1]


most_popular = soup.find(name='tr', id=highscore_id)
most_popular_link = most_popular.find(name='a', id='').get('href')
print(most_popular_link)