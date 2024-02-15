class Solution(object):
    def longestPalindrome(self, s):
        count, odd_count= Counter(s), 0
        for val in count:
            if count[val]%2 !=0:
                odd_count +=1

        if odd_count !=0:
            odd_count -=1
        return len(s) - odd_count 

       