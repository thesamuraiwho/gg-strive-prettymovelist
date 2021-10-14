# Data collected from
# https://strategywiki.org/wiki/Guilty_Gear_Strive/Moves under Creative
# Commons Attribution-ShareAlike

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from collections import OrderedDict

import pprint


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
                # Otherwise, the name is broken with <br/> elements and must be
                # constructed
                else:
                    for i in d.contents[0].contents:
                        if i.name == "br":
                            moveName += " "
                        else:
                            moveName += i
            # Move commands/inputs
            elif d['style'] == "text-align:right":
                command = []
                # Get the first element since the list only contains two and
                # the other is a '\n'
                e = d.contents[0]
                for f in e.descendants:
                    if f.name == "img":
                        command.append(f['src'])
                    # Text elements have no name, whereas others such as
                    # <small> and <a> do.
                    elif f.name is None and f.text != " ":
                        command.append((f.text).strip())
                charMoves[moveType][moveName] = command
            elif d['style'] == "color:white;width:80px;vertical-align:top;text-align:center;font-size:18px;padding:3px;text-shadow: black 1px 1px 3px":
                moveType = (d.text).lower().strip()


def generateCharMoveData(chars, setchars, chardir):
    """
    Combines characters names, move data, and image data into
    one structure.

    Parameters:
        chars: List of all character information
        setchars: bs4 element containing character move data and name
        chardir: List of character image paths

    Returns:
        None

    """


    count = 0
    while(count < len(setchars)):
        charName = setchars[count].contents[0]["id"].replace("_", " ")
        charMoves = {
            "command normals": OrderedDict(),
            "special attacks": OrderedDict(),
            "overdrives": OrderedDict()}

        findMoves(setchars[count + 1], charMoves)
        findMoves(setchars[count + 2], charMoves)

        img = "assets/char-imgs/gg-placeholder.jpg" # Default profile image
        displayName = charName.split(" ")[0].upper()

        # Search for character's profile image
        for i in chardir:
            # print(((i.split("/")[-1]).split(".")[0]).upper())
            if ((i.split("/")[-1]).split(".")[0]).upper() == displayName:
                img = i

        # Append character data to dict of characters
        chars.append({
            "fullName": charName,
            "displayName": displayName,
            "img": img,
            "moves": charMoves
        })

        count += 3 # Increment by 3 beautiful soup elements to the next character's section


def main():
    site = "https://strategywiki.org/wiki/Guilty_Gear_Strive/Moves"
    req = requests.get(site)

    pp = pprint.PrettyPrinter(indent=4)

    soup = BeautifulSoup(req.text, "html.parser")
    mainContent = soup.find("div", attrs={"class": "mw-parser-output"})

    # Removing the beginning and end of mainContent and getting the section
    # with moves
    mainContent.contents = mainContent.contents[4:223]

    # Removing the new lines
    mainContent.contents = [i for i in mainContent.contents if i != "\n"]

    # Removing <p><br></p>
    para = soup.new_tag("p")
    br = soup.new_tag("br")
    para.append(br)
    para.append("\n")

    mainContent.contents = [i for i in mainContent.contents if i != para]

    # Removing this element: <div style="clear: both;"></div>
    clearDiv = soup.new_tag("div")
    clearDiv['style'] = "clear: both;"

    mainContent.contents = [i for i in mainContent.contents if i != clearDiv]

    # Removing the div with the character's thumbnail <div class="floatright">
    floatDiv = soup.new_tag("div")
    floatDiv["class"] = "floatright"
    mainContent.contents = [
        i for i in mainContent.contents if i.names != "div" and i.attrs != {
            'class': ['floatright']}]

    baseChars = mainContent.contents[:45]
    dlcChars = mainContent.contents[46:]

    # chars = {}
    chars = []

    charImgsPath = "assets/char-imgs"
    chardir = os.listdir(charImgsPath)
    chardir.remove("gg-placeholder.clip")
    print(chardir)

    # WORKING LOOP
    generateCharMoveData(chars, baseChars, chardir)

    # count = 0
    # charNum = 0
    # while(count < len(baseChars)):
    #     charName = baseChars[count].contents[0]["id"].replace("_", " ")
    #     charMoves = {
    #         "command normals": OrderedDict(),
    #         "special attacks": OrderedDict(),
    #         "overdrives": OrderedDict()}

    #     findMoves(baseChars[count + 1], charMoves)
    #     findMoves(baseChars[count + 2], charMoves)
    #     # chars[charName] = charMoves

    #     img = "assets/char-imgs/gg-placeholder.jpg"
    #     displayName = charName.split(" ")[0].upper()
    #     for i in chardir:
    #         # print(((i.split("/")[-1]).split(".")[0]).upper())
    #         if ((i.split("/")[-1]).split(".")[0]).upper() == displayName:
    #             img = i

    #     chars.append({
    #         "fullName": charName,
    #         "displayName": displayName,
    #         "img": img,
    #         "moves": charMoves
    #     })

    #     count += 3


    generateCharMoveData(chars, dlcChars, chardir)

    # count = 0

    # while(count < len(dlcChars)):
    #     charName = dlcChars[count].contents[0]["id"]
    #     charMoves = {"command normals": OrderedDict(), "special attacks": OrderedDict(),
    #         "overdrives": OrderedDict()}

    #     findMoves(dlcChars[count + 1], charMoves)
    #     findMoves(dlcChars[count + 2], charMoves)
    #     # chars[charName] = charMoves
    #     img = "assets/char-imgs/gg-placeholder.jpg"
    #     displayName = charName.split(" ")[0].upper()
    #     for i in chardir:
    #         print(((i.split("/")[-1]).split(".")[0]).upper())
    #         if ((i.split("/")[-1]).split(".")[0]).upper() == displayName:
    #             img = i

    #     chars.append({
    #         "fullName": charName,
    #         "displayName": displayName,
    #         "img": img,
    #         "moves": charMoves
    #     })

    #     count += 3

    pp.pprint(chars)

    commandImgs = set()

    # Find all command image icons
    for char in range(len(chars)):
        for v in chars[char]['moves'].values():  # Move types (dicts)
            for v1 in v.values():  # Moves (lists)
                for i in range(len(v1)):  # Commands (strs)
                    if re.search(".png$", v1[i]):
                        commandImgs.add(v1[i])
                        v1[i] = f"assets/command-imgs/{v1[i].split('/')[-1]}"

    # Download all the command icons
    commandImgsPath = "assets/command-imgs"
    dir = os.listdir(commandImgsPath)
    # print(dir)

    # Check if the command images directory is empty or not
    if len(dir) == 0:
        print("Downloading command images.")
        for img in commandImgs:
            res = requests.get("https:" + img)
            shortenImg = img.split("/")[-1]
            print(shortenImg)
            with open(f"assets/command-imgs/{shortenImg}", "wb") as f:
                f.write(res.content)
    else:
        print("Skipping download for command images.")

    # Write out final json
    with open("gg-strive-moves.json", "w") as json_file:
        json.dump(chars, json_file, indent=2)

if __name__ == "__main__":
    main()
