# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    count = {}

    # buckets for nums key = num of occurrences, value = list of nums
    frequencies = [[] for x in range(len(nums) + 1)]

    for number in nums:
        count[number] = 1 + count.get(number, 0)

    for value, key in count.items():
        frequencies[key].append(value)

    result = []
    print(frequencies)

    for x in range(len(frequencies))[::-1]:
        for n in frequencies[x]:
            result.append(n)
            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
