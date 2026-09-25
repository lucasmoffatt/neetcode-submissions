class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1
        long = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            
            if nums[i] == nums[i+1] - 1:
                long += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                long = 1
            longest = max(long, longest)
                
        return longest
