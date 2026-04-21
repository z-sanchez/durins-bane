# Time Complexity: O(n), traverse the nodes
# Space Complexity: O(1), no space used


def findDuplicate(nums: List[int]) -> int:
    # Floyd's algo at play
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

        if slow2 == slow:
            return slow


if "__main__" == __name__:
    nums = [1, 2, 3, 2, 2]
    max = findDuplicate(nums)
    print("result", max)
