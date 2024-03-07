class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        l, r = 0, len(skill)-1
        chem=0
        skill_sum = 0
        while l < r:
            if l==0:
                skill_sum= skill[l]+skill[r]
                chem+=skill[l]*skill[r]
                
            else:
                if skill_sum != skill[l]+ skill[r]:
                    return -1
                else:
                    chem+= skill[l] * skill[r]
            l+=1
            r-=1
        return chem