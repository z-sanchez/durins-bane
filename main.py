# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    result = []
    count = {}

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    frequencies = [[] for x in range(len(nums) + 1)]

    for value, counted in count.items():
        frequencies[counted].append(value)

    for x in range(len(frequencies))[::-1]:
        for i in frequencies[x]:
            if len(result) >= k:
                return result
            else:
                result.append(i)

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
