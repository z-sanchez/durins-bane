# Time Complexity: O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    # for counting the occurrence of each num
    count = {}

    buckets = [[] for x in range(len(nums)+1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    print(count)

    for num, count in count.items():
        buckets[count].append(num)

    result = []

    for x in range(len(buckets))[::-1]:
        if len(result) >= k:
            return result

        for i in buckets[x]:
            result.append(i)

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 100]
    k = 2
    print(topKFrequent(nums, k))
