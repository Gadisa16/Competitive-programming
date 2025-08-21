/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let l = 0, r = height.length-1;
    let l_max = 0, r_max = 0, water = 0;

    while (l < r) {
        if (height[l] <= height[r]) {
            if (height[l] < l_max) {
                water = water + (l_max - height[l]);
            }
            else {l_max = height[l];}

            l++;
        }
        else {
            if (height[r] < r_max) {
                water = water + (r_max - height[r]);
            }
            else { r_max = height[r];}

            r--;
        }
    }
    return water
};