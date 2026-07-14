# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we make a set here

def groupAnagrams(strs):
    result = {}

    for str in strs:
        count = [0] * 26

        for s in str:
            count[ord(s) - ord('a')] += 1

        key = tuple(count)

        if key not in result:
            result[key] = []

        result[key].append(str)

    return list(result.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
