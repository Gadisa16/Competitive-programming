class Solution(object):
    def sortPeople(self, names, heights):
        dic= dict(zip(heights, names))
        sorted_dic= sorted(dic, reverse= True)

        return [dic[val] for val in sorted_dic]

        