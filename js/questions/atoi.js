const MIN = -2147483648
const MAX = 2147483647

var isNumber = (character) => character >= '0' && character <= '9';

var isInBound = (number) =>  number <= MAX && number >= MIN

var clampNumber = (number) => number < MIN ? MIN : MAX 


/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
    s = s.trim().toLowerCase();
    let sign = '+';
    let number = '0';
    for (let i = 0; i < s.length; i++) {
        if (i == 0) {
            if (s[0] == '-' || s[0] == '+') {
                sign = s[0];
            }else if(isNumber(s[0])){
                number += s[0]
            }else{
                break;
            }
        }else{
            if(isNumber(s[i]) || s[i] == '.'){
                number += s[i]
            }else{
                break;
            }
        }
    }
    number = parseFloat((sign+number))
    return isInBound(number) ? number : clampNumber(number);
};

// myAtoi('42')
// myAtoi('-42')
// myAtoi('4123 with words')
console.log(myAtoi("-91283472332"))