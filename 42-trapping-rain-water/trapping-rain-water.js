/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let l = 0, r = height.length, max_height = 1, water = 0;

    while (l < r) {
        if (height[l] <= height[r]) {
            if (max_height > height[l]) {
                water = water + (max_height - height[l]);
            }
            else {max_height = height[l];}

            l++;
        }
        else {
            if (max_height > height[r]) {
                water = water + (max_height - height[r]);
            }
            else { max_height = height[r];}

            r--;
        }
    }
    return water
};