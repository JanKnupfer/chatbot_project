var question;

function search(ele) {
    if(event.key === 'Enter') {
        question = ele.value;
        console.log(question);
    }
}

async function transferToRest() {

const params = {
    param1: question
};

let url = "http://127.0.0.1:8000/chatbotUI/api";
        async function transfer() {
            let response = await fetch(url, {
                mode: "no-cors",
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(params)
            })

            }

            }

transferToRest();
