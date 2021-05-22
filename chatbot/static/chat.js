

// Gets the first message
function firstBotMessage() {
    let firstMessage = "Hello😄 <br> my name is INU ON! <BR> Please question about INU!"
    document.getElementById("botStarterMessage").innerHTML 
    = '<li class="botText"><span>' + firstMessage + '</span></li>';
}

// HTML 생성이 완료된 후 firstBotMessage를 호출해야 
// document.getElementById("botStarterMessage")를 찾을 수 있습니다
$(document).ready(function() {
    firstBotMessage();
});


// Retrieves the response
function getHardResponse(userText) {
    
    let URL = 'https://inuon.run.goorm.io/chatbot/answer?'
    URL += 'content=' + userText
    
    fetch(URL, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function(resp) {
        let res = ''
        resp.json().then((result) => {
            res = result['res']

            let botResponse = res
            let botHtml = '<li class="botText"><span>' + botResponse + '</span></li>';
            $("#chatbox").append(botHtml);

            //document.getElementById("chat-bar-bottom").scrollIntoView(true);
        })
    })
}


//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textInput").val();

    let userHtml = '<li class="userText"><span>' + userText + '</span></li>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    
    getHardResponse(userText);
    
    //document.getElementById("chat-bar-bottom").scrollIntoView(true);
  
}

function getAnswer(userText) {
    
    let botResponse = getBotResponse(userText);
    let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

// Handles sending text via button clicks
function buttonSendText(sampleText) {

    let userHtml = '<li class="userText"><span>' + sampleText + '</span></li>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);

    getHardResponse(sampleText);

    //document.getElementById("chat-bar-bottom").scrollIntoView(false);

}


function sendButton() {
    getResponse();
}


// Press enter to send a message
$("#textInput").keypress(function (key) {
    if (key.which == 13) {
        getResponse();
    }
});