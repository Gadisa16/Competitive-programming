class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count, leng =0, len(citations)
        l, r =0, leng

        while l < r:
            mid = (l+r)//2

            if citations[mid] >=leng-mid:
                count =leng-mid
                r = mid
                
            else:
                l =mid+1
        return count
        