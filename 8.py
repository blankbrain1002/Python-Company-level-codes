from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())
 
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))