import { array } from "./puzzle_input";

let global = 0;

function isDigit(char){
    return char >= '0' && char <= '9'
}

array.forEach((str)=>{
    let dig = '';

    for(let i = 0 ; i < str.length ; i++){
        if(isDigit(str[i])){
            dig+= str[i]
            break;
        }
    }
    for(let i = str.length - 1; i >= 0 ; i--){
        if(isDigit(str[i])){
            dig += str[i]
            break;
        }
    }

    global += Number(dig)
})

console.log("Result ",global);