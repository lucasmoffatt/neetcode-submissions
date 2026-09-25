class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = {}
        ans = []
        unique = set()
        for i in range (len(nums) - 1):
            for j in range (i + 1, len(nums)):
                if (-(nums[i] + nums[j])) in indices:
                    a = [nums[i],nums[j], -(nums[i] + nums[j])]
                    a.sort()
                    if tuple(a) not in unique:
                        ans.append(a)
                        unique.add(tuple(a))
                    
                    
                indices[nums[j]] = j
            indices = {}
        
        return ans
        
       