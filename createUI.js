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

addCharacter();

fetch('gg-strive-chars.json')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        chars = data;
    });
// console.log(chars.length);