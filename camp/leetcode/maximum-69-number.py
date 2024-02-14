class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list= list(map(str, str(num)))
        for i in range(len(num_list)):
            if num_list[i]== "6":
                num_list[i] = "9"
                break
        str_num= "".join(num_list)
        return int(str_num)
            

        
        