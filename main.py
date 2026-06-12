# Time Complexity = O(m * n) n for the number of elements, m for the length of each char
# Space Complexity = O(m) for the map we create

def groupAnagrams(strs):

    # map will have a tuple as a key, then a list of strings for values
    map = {}

    # loop through list of words

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)

        if key not in map:
            map[key] = []

        map[key].append(word)

    return list(map.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
