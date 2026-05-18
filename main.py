# Time Complexity = O(m * n) n for the number of elements, m for the length of each char
# Space Complexity = O(m) for the map we create

def groupAnagrams(strs):
    map = {}

    for str in strs:
        counts = [0] * 26

        for char in str:
            counts[ord(char) - ord('a')] += 1

        key = tuple(counts)

        if key not in map:
            map[key] = []

        map[key].append(str)

    return list(map.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
