
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
    let map = {}
    let windowMap = {}
    for (const w of t) {
        map[w] = (map[w] ?? 0) + 1
        windowMap[w] = 0;
    }
    let l = 0, r = -1;
    let targetKeys = Object.keys(windowMap).length;
    let matchedKeys = 0;
    let subStringL = 0;
    let subStringR = 0;
    let windowSize = Number.MAX_SAFE_INTEGER;
    while (r < s.length && l < s.length) {
        if (matchedKeys == targetKeys) {
            let curWindowSize = r - l + 1;
            
            if (curWindowSize < windowSize) {
                windowSize = curWindowSize;
                subStringL = l
                subStringR = r;
            }
            
            if (s[l] in map) {
                windowMap[s[l]]--;
                if(windowMap[s[l]] < map[s[l]]){
                    matchedKeys--;
                }
            } 
            l++;
        } else {
            r++;
            if (s[r] in map && r < s.length) {
                windowMap[s[r]]++;
                if (windowMap[s[r]] == map[s[r]]) {
                    matchedKeys++;
                }
            }
        }
    }

    return windowSize == Number.MAX_SAFE_INTEGER ? '' : s.substring(subStringL, subStringR + 1)
};

minWindow("bbaa", "aba")