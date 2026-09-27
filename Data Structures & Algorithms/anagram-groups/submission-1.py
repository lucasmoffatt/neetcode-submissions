class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} #(array of letters, word)
        ans = []

        for word in strs:
            charArr = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                charArr[i] += 1
            charTuple = tuple(charArr)
            if charTuple not in map:
                map[charTuple] = []
            map[charTuple].append(word)
                
        
        for value in map.values():
            ans.append(value)
        
        return ans

