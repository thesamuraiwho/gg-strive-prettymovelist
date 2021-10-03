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
# print(mainContent.prettify())
# print(type(mainContent))

# print(mainContent.contents)
# print(len(mainContent.contents))

# Removing the beginning and end of mainContent and getting the section with moves
mainContent.contents = mainContent.contents[4:223]
# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i] == '\n'):
#         print(f"{i}\t{mainContent.contents[i]}")

# for i in range(5):
#     print(f"{i}\t{mainContent.contents[i]}")

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
# soup = BeautifulSoup()
para = soup.new_tag("p")
br = soup.new_tag("br")
para.append(br)
para.append("\n")
print(para)

# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i] == para):
#         print(f"{i}\t{mainContent.contents[i]}")

mainContent.contents = [i for i in mainContent.contents if i != para]

print(f"len of mainContent: {len(mainContent.contents)}")

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}\n\n")

# Removing this element: <div style="clear: both;"></div>

# soup = BeautifulSoup()
clearDiv = soup.new_tag("div")
clearDiv['style'] = "clear: both;"
print(clearDiv)

# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i] == clearDiv):
#         print(f"{i}\t{mainContent.contents[i]}")

mainContent.contents = [i for i in mainContent.contents if i != clearDiv]
print(f"len of mainContent: {len(mainContent.contents)}")

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}\n\n")

# Removing the div with the character's thumbnail

# <div class="floatright">

floatDiv = soup.new_tag("div")
floatDiv["class"] = "floatright"
print(floatDiv)

print(mainContent.contents[66])
print(f"\n\nmainContent.contents[66].name: {mainContent.contents[66].name}\n\nmainContent.contents[66].attrs: {mainContent.contents[66].attrs}")
# print(mainContent.contents[66].__dict__)
print("\n\n")
print(mainContent.contents[66].__dict__.keys())

# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i].name == "div" and mainContent.contents[i].attrs == {'class': ['floatright']}):
#       print(f"{i}\t{mainContent.contents[i]}\n\n")

mainContent.contents = [i for i in mainContent.contents if i.names != "div" and i.attrs != {'class': ['floatright']}]
print(f"len of mainContent: {len(mainContent.contents)}")

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}\n\n")

baseChars = mainContent.contents[:45]
dlcChars = mainContent.contents[46:]

charName = dlcChars[0].contents[0]["id"]
charMoves = {"normals": [], "specials": [], "overdrives": []}

# Normals and Specials
print(f"{1}\t{dlcChars[1]}\n\n{dlcChars[1].contents}\n\n{len(dlcChars[1].contents)}")

# for i in range(len(dlcChars[1].contents)):
#     print(f"{i}\n{dlcChars[1].contents[i]}\n\n")

# Overdrives
print("Overdrives")
# print(f"{2}\t{dlcChars[2]}\n\n{dlcChars[2].contents}\n\n{len(dlcChars[2].contents)}\n\n")

# for i in range(len(dlcChars[2].contents)):
#     if(dlcChars[2].contents[i] != "\n"):
#         print(f"{i}\n{dlcChars[2].contents[i]}\n\n")
#         print(f"{dlcChars[2].contents[i].contents}\nlen: {len(dlcChars[2].contents[i].contents)}")
#         for j in range(len(dlcChars[2].contents[i].contents)):
#             if(dlcChars[2].contents[i].contents[j] != "\n"):
#                 print(f"{dlcChars[2].contents[i].contents[j]}\n\n")

# print([i for i in dlcChars[2].contents if i != "\n"])
# print("\n\n")

# Finding move names and move commands
# for child in [i for i in dlcChars[2].contents if i != "\n"]:
#     # if child.name == "td":
#     for d in child.descendants:
#         # Use the "style" key to determine if a <td> is a name or commands
#         if d.name == "td" and d.has_attr("style"):
#             # print(f"{d}\n\n")
#             if d['style'] == "text-align:left":
#                 print(f"{d.text}\n\n")
#             elif d['style'] == "text-align:right":
#                 command = []
#                 # print(d.contents)
#                 for e in d.descendants:
#                     if e.name == "img":
#                         command.append(e['src'])
#                     elif e.name == "b":
#                         command.append(e.text)
#                 print(command)

for d in dlcChars[2].descendants:
    # Use the "style" key to determine if a <td> is a name or commands
    if d.name == "td" and d.has_attr("style"):
        # print(f"{d}\n\n")
        if d['style'] == "text-align:left":
            print(f"{d.text}\n\n")
        elif d['style'] == "text-align:right":
            command = []
            # print(d.contents)
            for e in d.descendants:
                if e.name == "img":
                    command.append(e['src'])
                elif e.name == "b":
                    command.append(e.text)
            print(command)

print(f"charName: {charName}")

# for i in range(len(dlcChars)):
#     if(dlcChars[i].name == "h3"): # DLC character name
#         print(f"{i}\t{dlcChars[i]}\n\n{dlcChars[i].contents}\n\n{dlcChars[i].contents[0]['id']}\n\n")
#     else:
#         print(f"{i}\t{dlcChars[i]}\n\n{dlcChars[i].contents}\n\n")


# characters = {}
# char = ""
# for i in dlcChars:
#     if i.name == "h3":
#         characters['name'] = i.contents[0]['id']
#         characters['moves'] = []
#     else:









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