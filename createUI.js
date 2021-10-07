// TODO: combine into ggStrive.json later
let globalData = [];

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
        newRadio.id = char.displayName;
        newRadio.value = char.displayName;
        newRadio.onclick = () => {
            if (newRadio.checked) {
                // console.log(char.moves);
                console.log(`globaldata: ${globalData}`);
                for(let i = 0; i < globalData.length; i++) {
                    if (globalData[i].displayName === newRadio.value) {
                        console.log(`globalData[${i}].displayName: ${globalData[i].displayName}\tnewRadio.value: ${newRadio.value}`);
                        createMoveList(globalData[i].moves);
                    }
                }
                console.log(newRadio.value);
            }
        };

        // Temporary default value. Should be the first value of a sorted list or something.
        if(char.displayName === "ANJI") {
            newRadio.checked = "checked";
            createMoveList(char.moves);
            // createMoveList(char.moves);
        }

        newLabel.appendChild(newRadio);

        let newImg = document.createElement("img");
        newImg.src = `${char.img}`;
        newImg.className = "char-thumbnail";
        newLabel.appendChild(newImg);
        const newName = document.createElement("p");
        const newText = document.createTextNode(`${char.displayName}`);
        newName.className = "bottom-left";
        newName.appendChild(newText);
        newLabel.appendChild(newName);
        const newBreak = document.createElement("br");
        newLabel.appendChild(newBreak);
        const charSection = document.getElementById("characterSelect");
        console.log(`charSection: ${charSection}`);
        charSection.appendChild(newLabel);
    });
}


function createMoveList(moves) {
    // console.log(moveList.moves);
    const moveList = document.getElementById("movelistMenu");
    console.log(`movelist.innerHTML: ${movelist.innerHTML}`);
    moveList.innerHTML = "";

    function createMove(moveCategory, category) {
        const moveDiv = document.createElement("div");
        const categoryType = document.createElement("h3");
        categoryType.appendChild(document.createTextNode(`${category}`));
        moveDiv.appendChild(categoryType);
        moveCategory.forEach(move => {
            const moveName = document.createElement("p");
            moveName.appendChild(document.createTextNode(`${move.moveName}`));
            moveDiv.appendChild(moveName);
            const buttons = document.createElement("p");
            buttons.appendChild(document.createTextNode(`${move.buttons}`));
            moveDiv.appendChild(buttons);
            // moveDiv.appendChild(document.createElement("br"));
    
            if(move.followup) {
                move.followup.forEach(fuMove => {
                    const fuMoveName = document.createElement("p");
                    fuMoveName.appendChild(document.createTextNode(`--> ${fuMove.moveName}`));
                    moveDiv.appendChild(fuMoveName);
                    const fuButtons = document.createElement("p");
                    fuButtons.appendChild(document.createTextNode(`${fuMove.buttons}`));
                    moveDiv.appendChild(fuButtons);
                    // moveDiv.appendChild(document.createElement("br"));
                });
            }
        });

        return moveDiv;
    }


    // const normalsDiv = document.createElement("div");
    // moves.normals.forEach(move => {
    //     const moveName = document.createElement("p").appendChild(document.createTextNode(`${move.moveName}`));
    //     normalsDiv.appendChild(moveName);
    //     const buttons = document.createElement("p").appendChild(document.createTextNode(`${move.buttons}`));
    //     normalsDiv.appendChild(buttons);

    //     if(move.followup) {
    //         move.followup.forEach(fuMove => {
    //             const fuMoveName = document.createElement("p").appendChild(document.createTextNode(`${fuMove.moveName}`));
    //             normalsDiv.appendChild(fuMoveName);
    //             const fuButtons = document.createElement("p").appendChild(document.createTextNode(`${fuMove.buttons}`));
    //             normalsDiv.appendChild(fuButtons);
    //         });
    //     }
    // });

    moveList.appendChild(createMove(moves.normals, "Command Normals"));
    moveList.appendChild(createMove(moves.specials, "Special Attacks"));
    moveList.appendChild(createMove(moves.overdrives, "Overdrives"));
    // const specialsDiv = document.createElement("div");
}

// function createMoveList(char) {
//     console.log(char.moves)
//     // createMove(char.moves);
// }

async function fetchJson(filename, func) {
    let response = await fetch(filename);
    let data = await response.json();
    globalData = data;
    func(data);
}

// addCharacter();

// fetchJson("gg-strive-chars.json", createCharsList);
fetchJson("gg-strive.json", createCharsList);
fetchJson("gg-strive.json", console.log);

// document.getElementsByName("chars").onclick = () => {
//     console.log(`char selection: ${document.querySelector('input[name="chars"]:checked')}`);
// }