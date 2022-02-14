function compara(num1, num2){

    let iguais = " não são";
    let soma = num1 + num2;
    let compara20 = "maior";
    let compara10 = "maior";

    if(num1 === num2){
        iguais = " são"
    }

    if(soma < 10){
        compara10 = "menor";
    }

    if(soma < 20){
        compara20 = "menor";
    }

    alert("Os numeros " + num1 + " e " + num2 + iguais + " iguais. Sua soma é " + soma + ", que é " + compara10 + " que 10 e " + compara20 + " que 20");
}

const num1 = Number(prompt());
const num2 = Number(prompt());

compara(num1, num2);