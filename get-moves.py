# Data collected from https://strategywiki.org/wiki/Guilty_Gear_Strive/Moves under  Creative Commons Attribution-ShareAlike
import requests
from bs4 import BeautifulSoup
import json
import re
from collections import OrderedDict

import pprint
pp = pprint.PrettyPrinter(indent=4)

def findMoves(char, charMoves):
    """
    Sifts through the DOM to retreive a character's move names and
    command inputs.

    Parameters:
        char (bs4 obj): bs4 element which contains a specific character's
            section of the DOM
        charMoves (dict): Dictionary containing all character move names
            and move inputs

    Returns:
        None
    """
    moveType = ""
    moveName = ""
    for d in char.descendants:
        # Use the "style" key to determine if a <td> is a name or commands
        if d.name == "td" and d.has_attr("style"):
            # print(f"{d}\n\n")
            if d['style'] == "text-align:left":
                # If the move name (first element of contents) only has one element,
                # it must be the whole name
                if len(d.contents[0].contents) == 1:
                    moveName = d.text.strip()
                # Otherwise, the name is broken with <br/> elements and must be constructed
                else:
                    for i in d.contents[0].contents:
                        if i.name == "br":
                            moveName += " "
                        else:
                            moveName += i
            # Move commands/inputs
            elif d['style'] == "text-align:right":
                command = []
                # Get the first element since the list only contains two and the other is a '\n'
                e = d.contents[0]
                for f in e.descendants:
                    if f.name == "img":
                        command.append(f['src'])
                    # Text elements have no name, whereas others such as <small> and <a> do.
                    elif f.name == None:
                        command.append((f.text).strip())
                charMoves[moveType][moveName] = command
            elif d['style'] == "color:white;width:80px;vertical-align:top;text-align:center;font-size:18px;padding:3px;text-shadow: black 1px 1px 3px":
                moveType = (d.text).lower().strip()

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

# Removing the div with the character's thumbnail <div class="floatright">

floatDiv = soup.new_tag("div")
floatDiv["class"] = "floatright"
print(floatDiv)

print(mainContent.contents[66])
print(f"\n\nmainContent.contents[66].name: {mainContent.contents[66].name}\n\nmainContent.contents[66].attrs: {mainContent.contents[66].attrs}\n")
# print(mainContent.contents[66].__dict__)
print(mainContent.contents[66].__dict__.keys())

# for i in range(len(mainContent.contents)):
#     if(mainContent.contents[i].name == "div" and mainContent.contents[i].attrs == {'class': ['floatright']}):
#       print(f"{i}\t{mainContent.contents[i]}\n\n")

mainContent.contents = [i for i in mainContent.contents if i.names != "div" and i.attrs != {'class': ['floatright']}]
print(f"len of mainContent: {len(mainContent.contents)}\n\n")

# for i in range(len(mainContent.contents)):
#     print(f"{i}\t{mainContent.contents[i]}\n\n")

baseChars = mainContent.contents[:45]
dlcChars = mainContent.contents[46:]

for i in range(len(dlcChars)):
    print(f"{i}\t{dlcChars[i]}\n\n")

chars = {}

for i in range(len(baseChars)):
    print(f"\n{i}\n{baseChars[i]}")

print("\n\n")

# ### Issue with millia (27) and ramlethal (36) command normals names.
# ### SOLUTION: Wasn't an issue at all. Just a print formatting thing.
# count = 24

# print(baseChars[count])
# print(baseChars[count + 1])
# print(baseChars[count + 2])

# charName = baseChars[count].contents[0]["id"]
# charMoves = {"command normals": OrderedDict(), "special attacks": OrderedDict(), 
#     "overdrives": OrderedDict()}

# findMoves(baseChars[count + 1], charMoves)
# findMoves(baseChars[count + 2], charMoves)
# print(charName)
# pp.pprint(charMoves)


### WORKING LOOP

count = 0
while(count < len(baseChars)):
    charName = baseChars[count].contents[0]["id"]
    charMoves = {"command normals": OrderedDict(), "special attacks": OrderedDict(), 
        "overdrives": OrderedDict()}

    findMoves(baseChars[count + 1], charMoves)
    findMoves(baseChars[count + 2], charMoves)
    chars[charName] = charMoves
    count += 3

count = 0

while(count < len(dlcChars)):
    charName = dlcChars[count].contents[0]["id"]
    charMoves = {"command normals": OrderedDict(), "special attacks": OrderedDict(), 
        "overdrives": OrderedDict()}

    findMoves(dlcChars[count + 1], charMoves)
    findMoves(dlcChars[count + 2], charMoves)
    chars[charName] = charMoves
    count += 3

pp.pprint(chars)
print(len(chars))
pp.pprint(chars['May'])
