class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0  # Current position in nums
        for group in groups:
            found = False
            # Try to find group starting at or after pos
            for i in range(pos, len(nums) - len(group) + 1):
                if nums[i:i+len(group)] == group:
                    pos = i + len(group)  # Update position to end of match
                    found = True
                    break
            if not found:
                return False
        return True