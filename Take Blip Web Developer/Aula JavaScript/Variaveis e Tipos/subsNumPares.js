function subsNumPares(arrayNum){

    if(arrayNum.length === 0){
        return -1;
    }
    for (let i = 0; i < arrayNum.length; i++) {
        if(arrayNum[i]%2 === 0 && arrayNum[i] !== 0){
            arrayNum[i] = 0;
        }
    }

    return arrayNum;
}

console.log(subsNumPares([2,3,4,4,5]));

