
function fibo(n){
    if(n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{
        return fibo(n-1)+fibo(n-2);
    }
}

function calcular(){

    const entrada =  document.querySelector("#entrada");

    document.querySelector("#saida").value = fibo(entrada.value);
}


function addLista(){

    // Armazenando elementos
    const item = document.querySelector("#item");
    const lista = document.querySelector(".listaElementos");
    const novoLi = document.createElement("li");

    //Criando elementos
    const novoCheckbox = document.createElement("input");
    novoCheckbox.type = 'checkbox';
    novoCheckbox.className = 'novoItem';
    const novoItem = document.createElement("label");
    novoItem.textContent = item.value;

    novoLi.appendChild(novoCheckbox);
    novoLi.appendChild(novoItem);

    lista.appendChild(novoLi);

    novoCheckbox.onclick = function(){
        var styleLabel = novoItem.style.textDecoration;
        if(styleLabel == ''){
            novoItem.style.textDecoration = 'line-through';
            
        }else{
            novoItem.style.textDecoration = '';
        }
    }
}





