function verificaPalindromo(palavra){

    let inversoPalavra = palavra.split("").reverse().join("")
    
    if(palavra === inversoPalavra){
        console.log("É palindromo")
    }else{
        console.log("Não é palindromo")
    }
}

verificaPalindromo("arara");

