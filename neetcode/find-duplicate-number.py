# Time Complexity: O(n), traverse the nodes
# Space Complexity: O(1), no space used


def findDuplicate(nums: List[int]) -> int:
    # Floyd's algo at play
    slow = 0
    fast = 0

    # pseudo do-while loop
    while True:
        # treat each value in the array as a pointer to the next in the list
        slow = nums[slow]

        # fast travels twice as far
        fast = nums[nums[fast]]

        # the pointers will inevitably meet if a cycle is present, this will be halfway in the cycle (fast is half the ways in front of slow)
        if slow == fast:
            break

    slow2 = 0

    # pseudo do-while loop
    while True:
        # advance the point where our last pointers met (halfway in cycle)
        slow = nums[slow]

        # advance from beginning of list
        slow2 = nums[slow2]

        # Floyd's algo will find the point where the start of the cycle begins
        # where the duplicate node exists
        # when the slow2 pointer meets the root of the cycle, our original slow pointer will travel
        # next half of cycle and meet it right on time
        if slow2 == slow:
            return slow


if "__main__" == __name__:
    nums = [1, 2, 3, 2, 2]
    max = findDuplicate(nums)
    print("result", max)
