# Time Complexity: O(n^2), nested loops
# Space Complexity: O(n), creating a result array

# The idea here is that you focus on one value at a time. Take that value and find what other two summed with it = 0. Then move to next index.
# We don't have to worry about comparing results using previous array values because those have been exhausted and check for
# Rule of thumb: Once we've passed an index in the array, those values have been checked if there in play already, no need to compare back

def topKFrequent(nums, k):
    result = []

    count = {}

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    frequencies = [[] for x in range(len(nums) + 1)]

    for key, value in count.items():
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
