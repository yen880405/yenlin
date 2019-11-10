class Solution(object):

    def __init__(self, nums):
        self.array = nums

    def merge_sort(self):
        if len(self.array) > 1:
            m = len(self.array)//2
            left = self.array[:m]
            right = self.array[m:]

            leftsorter = MergeSort(left)
            leftsorter.merge_sort()
            rightsorter = MergeSort(right)
            rightsorter.merge_sort()

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1
