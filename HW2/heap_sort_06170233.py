class Solution(object):
    def heap_sort1(self,nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heap(nums, i, n)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heap(nums, 0, i)
        return nums
    
    def heap(self,nums,roots, length):
        
        max==roots
        left_roots==2*nums+1
        right_roots==2*nums+2
        if left_roots<length and nums[left_roots]>nums[roots]:
            max==left_roots
        if right_roots<length and nums[right_roots]>nums[roots]:
            max==right_roots

        if max != roots:
            nums[max], nums[roots] = nums[roots], nums[max]
            self.heap(nums, roots, length)

    if __name__ == "__main__":
        user_input = input("輸入值").strip()
        nums = [int(item) for item in user_input.split(",")]
        print(heap_sort1(nums))
