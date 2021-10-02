import requests
from bs4 import BeautifulSoup
import json
import re

site = "https://strategywiki.org/wiki/Guilty_Gear_Strive/Moves"
req = requests.get(site)

# print(resp.text)
soup = BeautifulSoup(req.text, "html.parser")
# headlines = soup.find_all('h2', {'class': 'mw-headline'})
# print(headlines)
# print(soup.title)
# mainContent = soup.find("div", attrs={"id": "mw-content-text"})
mainContent = soup.find("div", attrs={"class": "mw-parser-output"})
print(mainContent.prettify())
print(type(mainContent))
# for c in mainContent.children:
#     print(c)

print(mainContent.contents)
print(len(mainContent.contents))

for i in range(len(mainContent.contents)):
    print(f"{i}\t{mainContent.contents[i]}")

mainContent.contents = mainContent.contents[:223]
print(type(mainContent.contents[0]))

# mainContent.contents = [i for i in mainContent.contents if re.match("\S", i)]#list(filter(lambda x: re.match("\S", x), mainContent.contents))

print(f"len of mainContent: {len(mainContent.contents)}")

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}")

# print(type(mainContent.contents[214]))
# print(mainContent.contents)

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}")



# for h in soup.find_all("span", attrs={"class": "mw-headline"}): # find_all(name, attrs, recursive, string, limit, **kwargs)
#     print(h.get("id"))

# print("\n\n")

# for h in soup.find_all("a", attrs={"href": re.compile("^/wiki/Guilty_Gear_Strive/")}): # find_all(name, attrs, recursive, string, limit, **kwargs)
#     print(h.contents[0])

# print("\n\n")

# for tbody in soup.find_all("tbody"):
#     print(tbody.contents)