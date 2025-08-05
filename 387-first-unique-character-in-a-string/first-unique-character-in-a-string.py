class Solution(object):
    def firstUniqChar(self, s):
        dic = OrderedDict()

        i = 0
        for ch in s:
            if ch not in dic:
                dic[ch] = [1, i]
            else:
                dic[ch][0] +=1
                
            i +=1

        for k in dic:
            freq, i = dic[k]
            if freq == 1:
                return i

        return -1

            
        



        
        