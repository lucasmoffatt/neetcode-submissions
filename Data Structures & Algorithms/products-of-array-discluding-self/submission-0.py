class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mult *= num
        
        if zero_count >= 2:
            return [0] * len(nums)

        # <= 1 zero
        if zero_count == 0:
            for i in range(len(nums)):
                nums[i] = mult // nums[i]
        else:
            for i in range (len(nums)):
                if nums[i] == 0:
                    nums[i] = mult
                else:
                    nums[i] = 0
        
        return nums
