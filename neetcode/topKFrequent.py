# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    count = {}

    # buckets for nums key = num of occurrences, value = list of nums
    frequencies = [[] for x in range(len(nums) + 1)]

    for n in nums:
        # incrementing the count for a num
        count[n] = 1 + count.get(n, 0)

    # magic happens here, using count of occurrences at key, appending value to bucket
    for value, key in count.items():
        # map to frequencies buckets
        frequencies[key].append(value)

    result = []

    # start at end of list, stop at [0], decrement by 1, going backwards starts us at most occurring nums
    for i in range(len(frequencies) - 1, 0, -1):
        # look through bucket
        for n in frequencies[i]:
            result.append(n)
            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, 1))
