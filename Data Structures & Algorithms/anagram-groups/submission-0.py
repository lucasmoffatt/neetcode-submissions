class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first is sorted, second is set of all
        dic = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1
            
            dic[tuple(count)].append(s)
            
        return list(dic.values())
        
            