/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    let c = b.split(a).length -1;

    for (let i = c; i <= c+2; i++) {
        if (a.repeat(i).includes(b)) {
            return i
        }
    }
    return -1
};