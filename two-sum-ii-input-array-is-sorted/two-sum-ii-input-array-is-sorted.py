class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for ind,num in enumerate(numbers):
            if (target-num) in dic:
                return([dic[target-num]+1, ind+1])
            dic[num] = ind
        