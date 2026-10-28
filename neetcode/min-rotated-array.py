# Time Complexity: logn
# Space Complexity: O(1)


def findMin(nums):
    # Using a binary search approach
    left = 0  # set your low/left
    right = len(nums) - 1  # set high/right
    result = nums[0]  # default the min to first of array

    while left <= right:  # binary search
        midpoint = (left + right) // 2  # solve midpoint

        # make the evaluation first to find min
        result = min(nums[midpoint], result)

        # if midpoint is greater than the right
        # it means everything left of the midpoint is also greater
        # than right due to the rotation
        if nums[midpoint] > nums[right]:
            left = midpoint + 1
        # if the midpoint were less than the right
        # there's lesser values to the left to
        # be explored
        else:
            right = midpoint - 1

    return result


if "__main__" == __name__:
    nums = [3, 4, 5, 6, 1, 2]

    print(findMin(nums))
