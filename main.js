var parentElement = document.querySelectorAll('div[data-testid="tweetText"]');
var textContent  = "";
for(let i = 0; i < parentElement.length; i++){
textContent += parentElement[i].textContent.trim();
}
return textContent