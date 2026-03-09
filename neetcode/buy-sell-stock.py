# Time Complexity: O(n), nested loops
# Space Complexity: O(1), same two pointers every time

def maxProfit(prices) -> int:
    # two pointer approach, one focus, one scouting ahead
    left = 0
    right = 1

    maxProfit = 0

    # run till scout meets end
    while right < len(prices):

        # left is where we buy, condition is true when profit possible
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        # if left is greater than right, means there's a new opportunity to by lower that we must now explore
        # we can update left because all other possibilities of profit have been explored
        else:
            left = right

        # always increment right to move the algo
        right += 1

    return maxProfit


if "__main__" == __name__:
    prices = [10, 1, 5, 6, 7, 1]

    result = maxProfit(prices)
    print(result)
