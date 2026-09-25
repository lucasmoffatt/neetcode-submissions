class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 1
        margin = 0 

        while sell_pointer < len(prices):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer

            profit = prices[sell_pointer] - prices[buy_pointer]
            if profit > margin:
                margin = profit

            sell_pointer += 1

        return margin            
            