class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, left_val= [0], height[0]
        for val in height[1:]:
            max_left.append(left_val)
            left_val =max(max_left[-1], val)
        
        max_right, right_val = [0], height[-1]
        for i in range(len(height)-2, -1, -1):
            max_right.insert(0, right_val)
            right_val = max(height[i], right_val)
        
        water_amount =0
        for i in range(len(height)):
            cur_amount =min(max_left[i], max_right[i])-height[i]
            if cur_amount >0:
                water_amount += cur_amount
        return water_amount         
            