class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twen= 0, 0, 0
        for dol in bills:
            if dol== 5:
                five +=1
            elif dol== 10:
                ten +=1
                if five>0:
                    five -=1
                else:
                    return False
            else:
                twen +=1
                if ten>0 and five>0:
                    ten, five = ten-1, five-1
                elif five >=3:
                    five -=3
                else:
                    return False
        return True
                    
                
            

        