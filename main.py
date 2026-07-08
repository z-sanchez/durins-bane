# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    frequencies = [[] for x in range(len(nums) + 1)]

    counts = {}

    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    for num, count in counts.items():
        frequencies[count].append(num)

    result = []

    print(frequencies)

    for x in range(len(frequencies))[::-1]:
        for j in frequencies[x]:
            if len(result) < k:
                result.append(j)
            else:
                return result

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, 1))
