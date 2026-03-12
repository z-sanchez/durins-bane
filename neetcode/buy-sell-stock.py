# Time Complexity: O(n), nested loops
# Space Complexity: O(1), same two pointers every time

def maxProfit(prices) -> int:
    # two pointer approach, one focus, one scouting ahead
    left = 0
    right = 1

    maxProfit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right

        right += 1

    return maxProfit


if "__main__" == __name__:
    prices = [10, 1, 5, 6, 7, 1]

    result = maxProfit(prices)
    print(result)
