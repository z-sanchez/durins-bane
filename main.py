import math


def groupAnagrams(strs):

    map = {}

    for word in strs:
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord('a')] += 1

        key = tuple(count)

        if key not in map:
            map[key] = []

        map[key].append(word)

    return list(map.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
