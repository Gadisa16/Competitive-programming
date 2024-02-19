class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_dic, ans= Counter(answers), 0
        
        for val in count_dic:
            ans += ceil(count_dic[val]/(val+1))*(val+1)

        return ans