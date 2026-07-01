def topKFrequent(nums, k):

    count = {}

    frequencies = [[] for x in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    print(count)

    for number, frequency in count.items():
        print(number, frequency)
        frequencies[frequency].append(number)

    print(frequencies)

    result = []

    for i in range(len(frequencies))[::-1]:
        for x in frequencies[i]:
            if len(result) >= k:
                return result
            else:
                result.append(x)

    return result


if __name__ == "__main__":
    nums = [7, 7]
    k = 1
    print(topKFrequent(nums, k))
