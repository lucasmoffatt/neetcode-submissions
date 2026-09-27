class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        freq = [ [] for _ in range (len(nums) + 1)]
        ans = []

        for num in nums:
            f[num] = f.get(num, 0) + 1
        
        for num, count in f.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans
                
