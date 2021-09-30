// TODO: combine into ggStrive.json later

function addCharacter() {
    const newDiv = document.createElement("div");
    console.log(`newDiv: ${newDiv}`);
    const newContent = document.createTextNode("New character!");
    console.log(`newContent: ${newContent}`);
    newDiv.appendChild(newContent);
    const charSection = document.getElementById("characters");
    console.log(`charSection: ${charSection}`);
    charSection.appendChild(newDiv);
}

function createCharsList(chars) {
    chars.forEach(char => {
        const newDiv = document.createElement("div");
        const newName = document.createElement("p");
        const newText = document.createTextNode(`${char.name}`);
        newName.appendChild(newText);
        newDiv.appendChild(newName);
        let newImg = document.createElement("img");
        newImg.src = `${char.img}`;
        newDiv.appendChild(newImg);
        const charSection = document.getElementById("characters");
        console.log(`charSection: ${charSection}`);
        charSection.appendChild(newDiv);
    });
}

async function fetchJson(filename, func) {
    let response = await fetch(filename);
    let data = await response.json();
    func(data);
}

// addCharacter();

fetchJson("gg-strive-chars.json", createCharsList);
fetchJson("gg-strive.json", console.log);