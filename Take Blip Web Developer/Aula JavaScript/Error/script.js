function verificaTamanhoArray(array, tamanho){
    
    try{
        if (!array && !tamanho) throw new ReferenceError('Sem Parametros');
        if (typeof(array) !== 'object' || typeof(tamanho) !== 'number') throw new TypeError('Array não é do tipo objeto ou tamanho não é do tipo Number');
        if(array.length !== tamanho) throw new RangeError('Tamanho invalido');
        
        return array;
    }catch(e){
        if(e instanceof ReferenceError){
            console.log("Insira Parametros");
        }else if(e instanceof TypeError){
            console.log("Verificar os tipos dos parametros inseridos");
        }else if(e instanceof RangeError){
            console.log("Verificar o tamanho correto do array");
        }
    }   
}
 const array = [1,2,3,4,5];
 console.log(verificaTamanhoArray(array, 5));