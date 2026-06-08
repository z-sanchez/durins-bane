# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):

    count = {}

    frequencies = [[] for x in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for number, count in count.items():
        frequencies[count].append(number)

    result = []

    for x in range(len(frequencies))[::-1]:
        for n in frequencies[x]:
            result.append(n)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, 1))
