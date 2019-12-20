class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary approach
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        two_sum = dict() # key is a num in nums, value is num's index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in two_sum:
                two_sum[nums[i]] = i
            else:
                return [two_sum[complement], i]
