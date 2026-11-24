"""
2. Best Time to Buy and Sell Stock
Easy
Problem: Given an array prices, where each element represents a stock's price on a particular day, determine the maximum profit you can make by buying once and selling on a later day.

If no profit is possible, return 0.

Clarification: The array is in chronological order, meaning each index represents the stock price on a successive day.

Example:
prices = [7, 1, 5, 3, 6, 4]
# Expected: 5

Function:
def maxProfit(prices):
    pass

Suggested time: 15–20 minutes
"""
def maxProfit(prices):
    all_profits = []
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            buy = prices[i]
            sell = prices[j]
            if buy < sell:
                profit = sell - buy
                all_profits.append(profit)
    if all_profits == []:
        return 0
    else:
        return max(all_profits)

test_prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]
print(f"The max possible profit is: {maxProfit(prices)}")


# Other implementation: current_max and maximum
"""
def maxProfit(prices):
    current_max = 0
    maximum = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            buy = prices[i]
            sell = prices[j]
            if buy < sell:
                current_max = sell - buy
            maximum = max(current_max, maximum)
    return maximum
"""

def maxProfitBetter(prices):
    profit_today = 0
    best_profit = 0
    lowest_buy_price = prices[0]
    for i in range(0, len(prices)):
        price_today = prices[i]
        if price_today < lowest_buy_price:
            lowest_buy_price = price_today
        profit_today = price_today - lowest_buy_price
        best_profit = max(profit_today, best_profit)
    return best_profit

pricesNew = [7, 1, 5, 3, 6, 4]
print(f"The max possible profit is (better): {maxProfitBetter(pricesNew)}")