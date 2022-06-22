var question;

function search(ele) {
    if(event.key === 'Enter') {
        question = ele.value;
        console.log(question);
    }
}

function transferToRest(){
const url = 'http://127.0.0.1:8000/chatbotUI/api';

let data = {
  param: question
}

var request = new Request(url, {
	method: 'POST',
	body: JSON.stringify(data),
	headers: new Headers()
});

fetch(request)
.then(function() {
    // Handle response we get from the API
})
}
transferToRest();


