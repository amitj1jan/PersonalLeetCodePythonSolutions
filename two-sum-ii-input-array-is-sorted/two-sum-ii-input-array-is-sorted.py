class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ind,num in enumerate(numbers):
            if (target-num) in numbers:
                ind2 = numbers.index(target-num)+1
                if ind+1 == ind2:
                    numbers.remove(num)
                    ind2 = numbers.index(num)+2
                    return([ind+1, ind2])
                else:
                    return([ind+1, ind2])
        