from bs4 import BeautifulSoup

with open('h.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.select('li a'))

form_tag = soup.find(name='input')
maxlength = form_tag.get("maxlength")
print(maxlength)

# print(soup.title.string)
# print(soup.prettify())

# print(soup.p)
# all_p_tags = soup.find_all(name='p')
# print(all_p_tags)

# all_anchor_tags = soup.find_all(name='a')
# for link in all_anchor_tags:
#     print(link.get('href'))
#     print(link.getText())

# heading = soup.find(name='h1', id='name')
# heading = soup.find_all(name='h1')
# for text in heading:
#     print(text.getText())

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

heading = soup.select(selector=".heading")
print(type(heading[0].getText()))