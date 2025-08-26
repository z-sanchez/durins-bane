# Time Complexity: O(n)
# Space Complexity: O(n)

def getIndices(nums, target):
    map = {}

    for index, value in enumerate(nums):
        diff = target - value

        if (diff in map):
            return [map[diff], index]
        else:
            map[value] = index

    return []


if __name__ == "__main__":
    # these must be least to greatest
    nums = [3, 4, 5, 6]
    target = 7

    # result must be least to greatest
    result = getIndices(nums, target)

    print(result)
