# Time Complexity: O(n)
# Space Complexity: O(n)

def getIndices(nums, target):
    # The trick is to only add key, value after they have been visited
    # [value]: index
    prevMap = {}

    for i, n in enumerate(nums):
        # calculating the difference let's us see if we have it in the table
        difference = target - n
        if difference in prevMap:
            # return least to greatest (works because nums is ordered)
            return [prevMap[difference], i]
        # if not, add it
        prevMap[n] = i

    # loop works because by the time we iterate to the greatest index needed, we for sure will have visited the least


if __name__ == "__main__":
    # these must be least to greatest
    nums = [3, 4, 5, 6]
    target = 7

    # result must be least to greatest
    result = getIndices(nums, target)

    print(result)
