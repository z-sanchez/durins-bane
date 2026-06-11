# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    count = {}

    frequencies = [[] for x in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    print(count)
    print(frequencies)

    for num, frequency in count.items():
        frequencies[frequency].append(num)

    result = []

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
    print(topKFrequent(nums, 2))
