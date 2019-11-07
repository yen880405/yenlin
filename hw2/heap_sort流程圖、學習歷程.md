![](https://github.com/yen880405/yenlin/blob/master/image/S__2064798.jpg)


**參考網址：https://github.com/TheAlgorithms/Python/blob/master/sorts/heap_sort.py






```python
def roots(roots):
    max==roots
    left_roots==2*index+1
    right_roots==2*index+2
   
```

看了很多影片釐清觀念後，上網參考一些程式碼之後，過了一段時間嘗試自己重新模擬重新修改編譯，一直發現有些問題
能理解左子節點等於母結點的2倍加1的位置，以此類推，右子節點為母節點2倍加2的位置


```python
def heapify(arr, length):
    if left_roots<length and arr[left_roots]>arr[roots]:
        max==left_roots
    if right_roots<length and arr[right_roots]>arr[roots]:
        max==right_roots

    if max != roots:
        arr[max], arr[roots] = arr[roots], arr[max]
        heapify(arr,length)
```

也能理解當左子節點大於母節點時且又小於length時，max要變左子節點值，
以此類推，右子節點大於母節點時且又小於length時，max要變右子節點值
且還要告訴這個程式碼，當max不等於母節點的時候，就要去跑去交換


```python
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
        heapify(arr, roots, length)
```

後來發現沒辦法拆開來寫，一定得合一起，慢慢修改似乎又變得跟網路參考類似


```python
def heap_sort(arr):
    n = len(arr) 
    k=n//2-1
    while(k>=0):
        k=k-1
        heap(arr, i, n)
    j=n-1    
    while (j>0):
        j=j-1
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, 0, i)
    return arr
```

自己改寫了一些東西有辦法運行了！原本很興奮，結果後來發現根本沒辦法又慢慢不自覺改回跟參考網站相似


```python
if __name__ == "__main__":
    user_input = input("輸入值").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(heap_sort(arr))
```

    輸入值4,3,6,5



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-262-92a48dffcbc0> in <module>()
          2     user_input = input("輸入值").strip()
          3     arr = [int(item) for item in user_input.split(",")]
    ----> 4     print(heap_sort(arr))
    

    <ipython-input-259-b7265c7a4160> in heap_sort(arr)
          4     while(k>=0):
          5         k=k-1
    ----> 6         heap(arr, i, n)
          7     j=n-1
          8     while (j>0):


    NameError: name 'i' is not defined

