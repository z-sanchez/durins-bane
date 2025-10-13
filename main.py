# Time Complexity = O(logn) the array looked at is halved every iteration
# Space Complexity = O(1), no space needed to search

def search(nums, target: int) -> int:

    left = 0
    right = len(nums) - 1

    while left <= right:
        midpoint = (right + left) // 2

        if nums[midpoint] < target:
            left = midpoint + 1
        elif nums[midpoint] > target:
            right = midpoint - 1
        else:
            return midpoint

    return -1


if "__main__" == __name__:
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    result = search(nums, target)
    print(result)
