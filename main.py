# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    counts = {}

    frequencies = [[] for x in range(len(nums) + 1)]

    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    for num, count in counts.items():
        frequencies[count].append(num)

    result = []

    for x in range(len(frequencies))[::-1]:
        for n in frequencies[x]:
            result.append(n)
            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
