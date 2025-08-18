/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const parentheses = [];
    const open = ["(", "{", "["];
    const closed = [")", "}", "]"];
    for (let i = 0; i < s.length; i++) {
        if (open.includes(s[i])) {
            parentheses.push(s[i])
        } else if (closed.includes(s[i])) {
            const popped = parentheses.pop(); 
            if (open.indexOf(popped) !== closed.indexOf(s[i])) {
                return false;
            }
        }
    }
    return parentheses.length === 0;
};
