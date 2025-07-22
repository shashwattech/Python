prices = [7,1,5,3,6,4]


def buyAndSell(prices):

    maxProfit = 0

    for i in range(len(prices)):

        for j in range(i+1, len(prices)):

            profit = (prices[j] - prices[i])

            if profit > maxProfit:

                maxProfit = profit

            
    return maxProfit


print(buyAndSell(prices))



# solution diddnt got accepted brecause of brute forec approach. Performance	❌ O(n²) — too slow for large inputs
 




    

