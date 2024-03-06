class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, val in enumerate(prices):
            while stack and val <= stack[-1][1]:
                prev_ind, prev_val =stack.pop()
                prices[prev_ind]= prev_val - val
            stack.append([i, val])
        return prices