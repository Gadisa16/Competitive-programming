/**
 * @param {number} k
 * @return {character}
 */
var kthCharacter = function(k) {
  let word = "a";
  while (word.length < k) {
    let temp = "";
    for (let ch of word) {
        let val = 97 + (ch.charCodeAt(0) - 97 + 1)%26;
        temp += String.fromCharCode(val);
    }
    word += temp;
  }
  return word[k-1];  
};