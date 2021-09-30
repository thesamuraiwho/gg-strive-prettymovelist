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
        const newLabel = document.createElement("label");
        const newRadio = document.createElement("input");
        newRadio.type = "radio";
        newRadio.name = "chars";
        newRadio.id = char.name;
        newRadio.value = char.name;

        // Temporary default value. Should be the first value of a sorted list or something.
        if(char.name === "ANJI") {
            newRadio.checked = "checked";
        }

        newLabel.appendChild(newRadio);
        const newName = document.createElement("p");
        const newText = document.createTextNode(`${char.name}`);
        newName.appendChild(newText);
        newLabel.appendChild(newName);
        let newImg = document.createElement("img");
        newImg.src = `${char.img}`;
        newLabel.appendChild(newImg);
        const newBreak = document.createElement("br");
        newLabel.appendChild(newBreak);
        const charSection = document.getElementById("characterSelect");
        console.log(`charSection: ${charSection}`);
        charSection.appendChild(newLabel);
    });
}


function createMove(moveList) {
    const newDiv = document.createElement("div");
}

function createMoveList(char, moves) {
    let moveList = [];

    for(let i = 0; i < moves.length; i++) {
        if (moves[i].name === char.name) {
            moveList = moves[i];
        }
    }

    createMove(moveList);

}

async function fetchJson(filename, func) {
    let response = await fetch(filename);
    let data = await response.json();
    func(data);
}

// addCharacter();

fetchJson("gg-strive-chars.json", createCharsList);
fetchJson("gg-strive.json", console.log);

document.getElementsByName("chars").onclick = () => {
    
}

console.log(`char selection: ${document.querySelector('input[name="chars"]:checked')}`);