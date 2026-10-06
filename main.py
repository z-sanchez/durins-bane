# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):

    count = {}
    result = []

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    frequencies = [[] for x in range(len(nums) + 1)]

    for key, value in count.items():
        print(key, value)
        frequencies[value].append(key)

    for x in range(len(frequencies))[::-1]:
        for n in frequencies[x]:
            if len(result) >= k:
                return result
            else:
                result.append(n)

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
