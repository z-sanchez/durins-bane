# Time Complexity = O(logn) the array looked at is halved every iteration
# Space Complexity = O(1), no space needed to search

def search(nums, target: int) -> int:

    low = 0
    high = len(nums) - 1

    while low <= high:
        # // ensures no floats will be used to index array
        midpoint = low + (high - low) // 2

        if nums[midpoint] == target:
            return midpoint

        elif nums[midpoint] < target:
            low = midpoint + 1
        else:
            high = midpoint - 1

    return -1


if "__main__" == __name__:
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    result = search(nums, target)
    print(result)
