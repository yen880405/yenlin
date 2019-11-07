class Heap_Sort(object):
    def heap_sort(self,nums):
    def heap(arr,roots, length):
        max==roots
        left_roots==2*arr+1
        right_roots==2*arr+2
        if left_roots<length and arr[left_roots]>arr[roots]:
            max==left_roots
        if right_roots<length and arr[right_roots]>arr[roots]:
            max==right_roots

        if max != roots:
            arr[max], arr[roots] = arr[roots], arr[max]
            heap(arr, roots, length)

    def heap_sort1(arr):
    
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heap(arr, i, n)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heap(arr, 0, i)
        return arr


    if __name__ == "__main__":
        user_input = input("輸入值").strip()
        arr = [int(item) for item in user_input.split(",")]
        print(heap_sort1(arr))
