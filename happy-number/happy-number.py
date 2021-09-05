class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        while(n not in hash_map):
            hash_map[n] = 1
            n = sum([int(num)**2 for num in str(n)])
        return(n==1)
            
        
    
    
    