
function getAdmins(usuarios){

    for ([key, value] of usuarios) {
        if(value === 'Adm'){
            console.log(key);
        }
    }
}

function valoresUnicos(array){
    const semRepetir = new Set(array);

    return [...semRepetir];
}



const array = [30, 30, 40, 5, 223, 2049, 3034, 5];
const usuarios = new Map();

usuarios.set('Luiz','Adm');
usuarios.set('Maria','User');
usuarios.set('Pedro','User');
usuarios.set('Jose','User');
usuarios.set('Marta','Adm');
usuarios.set('Felipe','Adm');

getAdmins(usuarios);
console.log(valoresUnicos(array));