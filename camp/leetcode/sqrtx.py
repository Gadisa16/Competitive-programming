class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, ceil(1 + x/2)
        while l <= r:
            mid = (l+r)/2

            if int(mid**2) ==x:
                return int(mid)
            if x < mid**2:
                r =mid
            else:
                l =mid


        