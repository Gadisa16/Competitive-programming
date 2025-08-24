/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let len = nums.length;
    if (len === 1) return true;
    
    let pos = len-1;
    for (let i = len-2; i>=0; i--) {
        if (i+nums[i] >= pos) {
            pos = i;
            if (i == 0) return true;
        }
    }
    return false;
};