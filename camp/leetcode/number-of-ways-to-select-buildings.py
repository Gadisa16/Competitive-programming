class Solution:
    def numberOfWays(self, s: str) -> int:
        p_one, p_z= [int(s[0])], [1-int(s[0])]

        for val in s[1:]:
            p_one.append(p_one[-1] + int(val)) 
       
        for val in s[1:]:
            p_z.append(p_z[-1] +1-int(val))

        count, leng =0, len(s)
        for i in range(1, leng-1):
            val =int(s[i])
            if val == 1:
                count += p_z[i-1]* (p_z[-1]- p_z[i])
            else:
                count += p_one[i-1]* (p_one[-1]- p_one[i]) 
        return count