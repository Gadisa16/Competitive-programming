/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let l = 0, prod = 1, count = 0; 
    for (let r = 0; r < nums.length; r++){
        prod = prod*nums[r];

        while (prod >= k && l<=r){
            prod = prod / nums[l];
            l = l + 1;
        }

        count = count + r - l + 1;
    }
    return count;
};