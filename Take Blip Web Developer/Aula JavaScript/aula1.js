// FUNÇÃO

function fibo(n){
    if(n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{

        return fibo(n-2)+fibo(n-1);
    }
}

// Print no console
console.log(fibo(8));

// Executar no terminal node 'nome do arquivo'