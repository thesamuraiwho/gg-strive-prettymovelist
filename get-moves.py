# Data collected from https://strategywiki.org/wiki/Guilty_Gear_Strive/Moves under  Creative Commons Attribution-ShareAlike
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

print(mainContent.contents)
print(len(mainContent.contents))

# Removing the end of mainContent
mainContent.contents = mainContent.contents[:223]
# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i] == '\n'):
#         print(f"{i}\t{mainContent.contents[i]}")

# Removing the new lines
mainContent.contents = [i for i in mainContent.contents if i != "\n"]
# print(mainContent.contents)
# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}")
    
print(f"len of mainContent: {len(mainContent.contents)}")

# Removing <p><br></p>
print(mainContent.contents[115])
print(mainContent.contents[115].contents)
print(type(mainContent.contents[115]))
# Create a matching tag but something is different
soup = BeautifulSoup()
para = soup.new_tag("p")
br = soup.new_tag("br")
para.append(br)
para.append("\n")
print(para)

for i in range(len(mainContent.contents)):
    if(mainContent.contents[i] == para):
        print(f"{i}\t{mainContent.contents[i]}")

mainContent.contents = [i for i in mainContent.contents if i != para]

print(f"len of mainContent: {len(mainContent.contents)}")

# print(type(mainContent.contents[0]))

# mainContent.contents = [i for i in mainContent.contents if re.match("\S", i)]#list(filter(lambda x: re.match("\S", x), mainContent.contents))

# print(f"len of mainContent: {len(mainContent.contents)}")

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