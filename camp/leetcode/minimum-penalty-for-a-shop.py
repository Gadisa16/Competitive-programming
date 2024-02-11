class Solution(object):
    def bestClosingTime(self, customers):
        cleng= len(customers)
        pleng= cleng +1
        pref, postf= [0]*pleng, [0]*pleng

    #it counts the "N" before closing position (when shop is open)
        for i in range(1, pleng): # i is closing postion
            if customers[i-1]=="N":
                pref[i] += pref[i-1] +1
            else:
                pref[i] =pref[i-1]
        
        for i in range(pleng-2, -1, -1):
            if customers[i]=="Y":
                postf[i] +=postf[i+1] +1
            else:
                postf[i] = postf[i+1]
        
        min_pen, ind = float("inf"), 0
        for i in range(pleng):
            cur_pen= pref[i] + postf[i]
            if cur_pen < min_pen:
                min_pen = cur_pen
                ind= i
        return ind


            

            

        

        
        