const meuArray = [1,2,3,4,5,6];
const obj = {value: 10};

function mapThis(arr, thisArg){
    return arr.map(function(item){
        return item * this.value;
    }, thisArg);
}


// Map
console.log(mapThis(meuArray, obj));
console.log(meuArray.map((item) => item * 10));

// Filter
console.log(meuArray.filter((item) => item%2 === 0));

// Reduce
const precos = [14.2, 5.3, 32.4, 10];
const saldo = 100;

console.log(meuArray.reduce((prev, current) => prev + current));
console.log(precos.reduce((prev, current) => prev - current, saldo));