const x= 3;
const y= 4;

if(x==3 && y==4){
    console.log(true);
}

//${variabili}

const aName = ['pippo','pluto','paperino'];


for (let i=0; i<aName.length;i++){
    console.log('ciao '+ aName[i]);
    
}

function topolino (par1,par2){
    console.log(par1+' & '+par2)

}

topolino(aName[0],aName[1]);

const divEl1= document.getElementById('elem1');
console.log(divEl1.innerText);
//divEl1.style.color='red';
divEl1.classList.add('classe');
//creo oggetto in pg
const container =document.getElementById('cont');
const newDiv = document.createElement('div');
newDiv.innerText="ciao added div";
newDiv.classList.add('classe');
container.appendChild(newDiv);

//
const btn = document.getElementById('btn');
btn.addEventListener('click',function() {
    console.log('playyyy');
});
//
setTimeout(function(){
    console.log('scaduto');
},5000);

setInterval(function(){
    console.log('bipobipo')
},3000);



const timer1 = document.getElementById('mytimer');
let startsec = 10;

const clock = setInterval(function(){
    if (startsec==0) {
        timer1.innerText = "kaboom";
        //clearInterval(clock);
        startsec=10;
    } else {
        timer1.innerText=startsec;
        startsec--;
    }
},1000);

