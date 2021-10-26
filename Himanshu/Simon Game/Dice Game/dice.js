var randomNumber1 = Math.floor(Math.random()*6)+1;
var randomNumberDice = "dice"+randomNumber1+".png";
var randomDiceImg1 = "images/"+ randomNumberDice;
document.querySelectorAll("img")[0].setAttribute("src",randomDiceImg1);
var randomNumber2 =  Math.floor(Math.random()*6)+1;
var randomNumberDice = "dice"+randomNumber2+".png";
var randomDiceImg2 = "images/"+ randomNumberDice;
document.querySelectorAll("img")[1].setAttribute("src",randomDiceImg2);
if(randomNumber1>randomNumber2){
    document.querySelector("h1").innerHTML="🪐Player 1 won";

    var win = new Audio ("nani_Pmxf5n3.mp3"); 
    win.play();
}
 else if(randomNumber1<randomNumber2){
    document.querySelector("h1").innerHTML="🗽Player 2 won";
    var valo = new Audio("Aaron+Smith+Dancin+KRONO+Remix (2).mp3");
    valo.play();
}
else{
    document.querySelector("h1").innerHTML="🏳Draw";
    
}