class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         '''
             Brute Force Solution:
             • Time: O(n²) -> we are using nested for loops to find the max_profit
                             may not pass each and every test cases and timeouts in large inputs.
             • Space: O(1) -> only variables are used to solve this problem. 
                             and no other data structure is used. 
             • Start with this approach in a Live interview and then move to optimize it if asked.  
         '''
        max_profit = 0
        
        # Looping through the buying prices.
        for i in range(len(prices)):
            # Nested loop for iterating through selling prices.
            for j in range(i+1, len(prices)):

               # Profit = selling price - buying price.
                profit = prices[j] - prices[i]

                # Get the maximum value from profit and max_profit
                max_profit = max(profit, max_profit)

        # Return max profit if present else return 0.
        return max_profit 



class Solution:
    def maxProfit(self, prices: []) -> int:
        '''
            Optimized solution: Single pass Approach
            • Time: O(n) -> We're keeping track of the minimum prices seen so far.
                            And also computing the profit for each potential sell day.

            • Space: O(1) -> No additional data structure besides variables min_price and max_profit. 
        '''
        # Handle the edge case of an empty array.
        if not prices: return 0
        
        # Initialize mininmum price to be the first day's price.
        min_price = prices[0]

        # Initialize max_profit as 0. 
        # If no profit is possible return instead of -inf. 
        max_profit = 0

        # Iterating through prices starting from the 2nd element.
        # Since min_price is set to prices[0], we process subsequent prices to check 
        # for potential profits.
        for price in prices[1:]:

            # Since a lower price can lead to a higher profit.
            if price < min_price:
                min_price = price # update the minimum price if current price is lower.

            # This block executes when price > min_price    
            else:   
                # compute profit & update max_profit if this profit is larger.
                # profit = price - min_price.
                max_profit = max(max_profit, price - min_price)
        
        # After the loop, max_profit holds the highest profit(or 0 if no profit is available).  
        return max_profit 

            
