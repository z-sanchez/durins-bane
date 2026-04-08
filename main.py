# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string
def findDuplicate(nums: List[int]) -> int:
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


if "__main__" == __name__:
    nums = [1, 2, 3, 2, 2]
    max = findDuplicate(nums)
    print("result", max)
