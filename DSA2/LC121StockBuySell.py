prices = [7,1,5,3,6,4]


def maxPotential(prices):


    maxProfit = 0
    minPrice = float('inf')

    for price in prices:

        if price< minPrice:

            minPrice = price

        else:

            profit = price  - minPrice

            if profit>maxProfit:

                maxProfit = profit

    return maxProfit
        


print (maxPotential(prices))





# prices = [7, 1, 5, 3, 6, 4]

# def maxPotential(prices):
#     maxProfit = 0                      # Initialize max profit to 0
#     minPrice = prices[0]              # Start by assuming first price is the lowest

#     for price in prices:              # Loop through each price
#         if price < minPrice:          # If current price is less than min seen so far
#             minPrice = price          # Update minPrice
#         else:
#             profit = price - minPrice    # Calculate profit if bought at minPrice
#             if profit > maxProfit:       # If this profit is better than current best
#                 maxProfit = profit       # Update maxProfit

#     return maxProfit                   # Return the best possible profit

# print(maxPotential(prices))




