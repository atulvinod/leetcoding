/**
 * https://leetcode.com/problems/decode-string/submissions/
 */
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {

    function solve(str, start, end) {
        //overall result
        let result = ''

        //current count to track the number of times a string has to 
        //be multiplied to add to the result
        let currentCount = ''


        for (let i = start; i <= end; i++) {

            //we follow the bracket count approach to find the end bracket and 
            //we recursively call the function on the substring within the brackets
            //which is then multiplied with the currentCount.
            //when we find an opening bracket, we increase the count and for closing 
            //we decrease the count to indicate a bracket pair
            //if the number becomes less than zero, then there are no bracket pairs
            if (str[i] == '[') {
                let bracket_end_index = i + 1
                let bracket_count = 1
                while (bracket_end_index <= end) {
                    if (str[bracket_end_index] == '[') {
                        bracket_count++;
                    } else if (str[bracket_end_index] == ']') {
                        bracket_count--;
                    }

                    if (bracket_count <= 0) {
                        break;
                    }
                    bracket_end_index++;
                }

                let chars = solve(str, i + 1, bracket_end_index - 1)
                result += chars.repeat(Number(currentCount));
                currentCount = ''
                i = bracket_end_index
            } else if (str[i] >= '0' && str[i] <= '9') {
                currentCount += str[i]
            } else {
                result += str[i]
            }
        }
        return result;
    }

    return solve(s, 0, s.length - 1);
};

let z = '2[abc]3[cd]ef'
console.log(decodeString(z))