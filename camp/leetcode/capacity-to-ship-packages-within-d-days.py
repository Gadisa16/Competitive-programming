class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)  # Takes many days(needs may ships)
        max_cap = sum(weights)  # Takes few days(needs a few ships)
        ships =days

        while min_cap < max_cap:
            mid_cap = (min_cap + max_cap) // 2
            curw, count, i = 0, 1, 0
            while i < len(weights):
                if curw + weights[i] <= mid_cap:
                    curw += weights[i]
                    i += 1
                else:
                    curw = 0
                    count += 1

            if count <= ships:
                max_cap = mid_cap
            else:
                min_cap = mid_cap + 1
        return max_cap #return min_cap ,both are possible
