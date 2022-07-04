let question;
let answer;
let link;

function search(ele) {
    if (event.key === 'Enter') {
        question = ele.value;
        console.log(question);
        transferToRest();
    }
}

async function transferToRest() {
    const url = 'http://127.0.0.1:8000/chatbotUI/api';

    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        "question": question
    });

    const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw
    };


    if(question === ''){
    answer = "Bitte stelle mir eine richtige Frage!"}
    else{
    var response = await fetch(url, requestOptions);
    var data = await response.json();
    data = JSON.parse(data);
    //Statusabfrage
    if(data.statuscode === '404'){
    answer = "Leider gibt es dazu keine Anwort!";
    }
    else{
    answer = data.answer;
    }
    if(data.link !== ''){
    link = data.link;
    document.getElementById('link').innerHTML = link;
    document.getElementById('link').href = link;
    var div = document.getElementById("visible");
    div.style.visibility = 'visible';
    }
    else{
    var div = document.getElementById("visible");
    div.style.visibility = 'hidden';
    }
    }
    document.getElementById('question').innerHTML = question;
    document.getElementById('answer').innerHTML = answer;
    document.getElementById("send").value = "";
}
