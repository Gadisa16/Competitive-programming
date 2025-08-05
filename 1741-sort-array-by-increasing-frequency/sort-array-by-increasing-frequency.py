class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cd = Counter(nums)
        sorted_cd = dict(sorted(cd.items(), key= lambda x: (x[1], -x[0])))

        res = []
        for k in sorted_cd:
            res += [k]*sorted_cd[k]
            
        return res