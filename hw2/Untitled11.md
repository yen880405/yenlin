
邏輯釐清看了許多影片，大概畫了邏輯圖。總之就是，把一個數列拆拆拆拆分成兩個兩個一組，最後再慢慢比大小結合比大小結合直到結束。


```python
def k(arr):
    step=2
    a=[arr[i:i+step] for i in range(0,len(arr),step)]
    return a
```

這一串初學者的我大概卡了1小時，上網利用關鍵字找到這個切成兩個兩個一塊的方式


```python
arr=[3,1,12,14,26,22,33,34,50,52]
```


```python
print (k(arr))
```

    [[3, 1], [12, 14], [26, 22], [33, 34], [50, 52]]



```python
aa=k(arr)
```

原本直接用len(k(arr))後來發現這樣是不可行的，需要套入一個新變數名稱


```python
n=len(aa)
for i in range (0,n-1):
    h=len(aa[i])
    for j in range (0,h-1):
        if (aa[i][j]>aa[i][j+1]):
            m=aa[i][j+1]
            aa[i][j+1]=aa[i][j]
            aa[i][j]=m
```

想要讓他們倆倆先比大小再結合再比大小，但光這個for迴圈上網重複查詢，嘗試了又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯又嘗試又錯大概輸出200遍大概3小時，總算邏輯稍微成功，跑出來下列結果。


```python
print(aa)
```

    [[1, 3], [12, 14], [22, 26], [33, 34], [50, 52]]



```python

```


      File "<ipython-input-14-1e818f42ce49>", line 1
        def mergeList(aa[i][j], aa[i+1][j]):
                        ^
    SyntaxError: invalid syntax




```python
y=len(aa)
w=[r for r in aa [0:y//2]]
z=[e for e in aa[y//2:y]]
```


```python

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-265-5f086f96adf7> in <module>()
          1 for i in aa:
    ----> 2     r=aa[i]+aa[i+1]
    

    TypeError: list indices must be integers or slices, not list



```python
ii=[]
for uu in w:
    if isinstance(uu,list):
        for rr in uu:
            ii.append(rr) 
```


```python
ii
```




    [1, 3, 12, 14]




```python
kk=[]
for u in z:
    if isinstance(u,list):
        for r in u:
            kk.append(r)
```


```python
kk
```




    [22, 26, 33, 34, 50, 52]




```python
def mergeList(ii, kk):

   
     if len(ii) == 0: 
         return kk
     elif len(kk) == 0: 
         return ii
   
     elif ii[0] < kk[0]:
         return [ii[0]] + mergeList(ii[1:], kk)
     
     else: 
         return [kk[0]] + mergeList(ii, kk[1:])
```


```python
print( mergeList(ii, kk))
```

    [1, 3, 12, 14, 22, 26, 33, 34, 50, 52]



```python

```




    [[], None]




```python

```




    []


