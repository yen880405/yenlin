class Solution(object): 
    
    def heap_sort(self,nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heap(nums, i, n)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heap(nums, 0, i)
        return nums
    
    def heap(self, nums, roots, length):
        
        
        max=roots
        left_roots=2*roots+1
        right_roots=2*roots+2
        
        if left_roots<length and nums[left_roots]>nums[roots]:
            max=left_roots
        if right_roots<length and nums[right_roots]>nums[roots]:
            max=right_roots

        if max != roots:
            nums[max], nums[roots] = nums[roots], nums[max]
            self.heap(nums, roots, length)
   
