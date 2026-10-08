# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def topKFrequent(nums, k):

    result = []

    count = {}

    for x in nums:
        count[x] = 1 + count.get(x, 0)

    frequencies = [[] for x in range(len(nums) + 1)]

    for value, counted in count.items():
        frequencies[counted].append(value)

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
