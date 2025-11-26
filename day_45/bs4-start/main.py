from bs4 import BeautifulSoup


with open("website.html") as website:
    content = website.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# a_tags = soup.find_all(name="a")
# print(a_tags)
#
# for tag in a_tags:
#     print(tag.get("href"))
#
# heading = soup.find("h1", id="name")
# print(heading)
#
# section_heading = soup.find("h3", class_="heading")
#
# print(section_heading.text)

company_url = soup.select_one("p a")

print(company_url)

headings = soup.select(".heading")

print(headings)
