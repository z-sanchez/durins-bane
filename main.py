def topKFrequent(nums, limit):

    frequencies = [[] for x in range(len(nums) + 1)]

    counts = {}

    result = []

    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    for num, count in counts.items():
        frequencies[count].append(num)

    for i in frequencies[::-1]:
        for j in i:
            if len(result) >= limit:
                return result
            else:
                result.append(j)

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
