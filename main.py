# Time Complexity: O(n)
# Space Complexity: O(n)

def groupAnagrams(strs):

    mapping = {}

    for str in strs:
        count = [0] * 26

        for char in str:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)

        if key not in mapping:
            mapping[key] = []

        mapping[key].append(str)

    return list(mapping.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
