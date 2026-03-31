const messagesDiv = document.getElementById('messages');

function addMsg(sender, text) {
    const div = document.createElement('div');
    div.className = sender === "Bot" ? "bot-msg" : "user-msg";
    div.innerText = text;
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function handleChoice(choice) {
    if (choice === '1') {
        addMsg("You", "Track Package");
        addMsg("Bot", "Please enter your 8-digit Tracking ID in the console (or prompt).");
        let id = prompt("Tracking ID:");
        addMsg("Bot", id.length === 8 ? "Status: In Transit." : "Invalid ID format.");
    } 
    else if (choice === '2') {
        addMsg("You", "Product Advice");
        addMsg("Bot", "Laptops or Tablets? (Refresh to restart)");
    }
    else if (choice === '3') {
        addMsg("You", "Tech Support");
        addMsg("Bot", "Is the power light on? (Yes/No)");
    }
}