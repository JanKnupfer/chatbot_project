let question;

function search(ele) {
    if (event.key === 'Enter') {
        question = ele.value;
        transferToRest();
    }
}

async function transferToRest() {
    const url = 'http://127.0.0.1:8000/chatbotUI/api';

    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        "question": "question"
    });

    const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw
    };

    await fetch(url, requestOptions)
        .then(response => response.json())
        .catch(error => console.log('error', error));

}
