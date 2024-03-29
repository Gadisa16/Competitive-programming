class Solution:
    def sortSentence(self, s: str) -> str:
        word_list= s.split()
        oput= [None]*len(word_list)
        
        for word in word_list:
            index= int(word[-1]) -1
            oput[index]= word[:-1] #to exclude the last char(number)
        
        return " ".join(oput)
                  
"""index= word[-1] -1 #since the number at end of each words start from 1 we substract 1 to insure that it starts from 0 index."""