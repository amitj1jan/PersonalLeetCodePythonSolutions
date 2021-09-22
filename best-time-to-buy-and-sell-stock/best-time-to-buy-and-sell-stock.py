class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_prof = 0
        max_prof = 0
        buy = +inf
        for price in prices:             
            curr_prof = price-buy
            max_prof = max(max_prof, curr_prof)
            buy = min(buy, price)
        return(max_prof)
            