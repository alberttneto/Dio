function calculadora(num1, num2, op){

    console.log(op);
    switch(op){
        case 1: return num1 + num2;
        break;
        
        case 2: return num1 - num2;
        break;

        case 3: return num1 * num2;
        break;

        case 4: return num1 ** num2;
        break;

        default: alert("Opção incorreta");
        break;
    }
}

const operacao = Number(prompt("Informe operação: \n 1-(+)\n 2-(-)\n 3-(*)\n 4-(**)"));
const num1 = Number(prompt("Informe numero 1: "));
const num2 = Number(prompt("Informe numero 2: "));

alert("Resultado: " + calculadora(num1, num2, operacao));