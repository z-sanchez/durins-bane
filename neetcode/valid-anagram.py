# Time Complexity = O(n)
# Space Complexity = O(n + m)

def isAnagram( s: str, t: str) -> bool:
        # anagrams must be same length
        # if we were to check each length manually time complexity would be O(n+m)
        if len(s) != len(t):
            return False

        # dictionaries for tracking frequency of characters
        # this could also be considered O(n+m) space complexity because we need space for both at different sizes
        # but here we know they will be the same length and won't grow independently
        countS, countT = {}, {}

        for i in range(len(s)):
            # update the frequency in the map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print(countS, countT)
        # this line checks if they have same key/pairs (order doesn't matter)
        return countS == countT


result = isAnagram("jar", 'rja')
print("Is anagram:", result)