# 簡介
集合 (Set) 其實和數組 (Tuple) 與串列 (List) 很類似, 不同的點在於集合不會包含重複的資料

# 概述

宣告與建立集合 (Set)
set1 = set()# 建立空的集合

set2 = {1, 2, 3, 4, 5}

# 從串列 (List) 來建立集合
set3 = set([i for i in range(20, 30)])

# 從數組 (Tuple) 來建立集合
set4 = set((10, 20, 30, 40, 50))

# 集合不會包含重複的資料, 你可以從 set5 印出來的結果得知
set5 = set((1, 1, 1, 2, 2, 3))

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
注意： 建立空集合的方法是 set1 = set() 而不是 set1 = {}



集合加入與刪除元素
可以使用 add(value) 來加入新元素, 也可以使用 remove(value) 來移除元素

set2 = {1, 2, 3, 4, 5}
set4 = set((10, 20, 30, 40, 50))

set2.add(6) # 在 set2 中加入 6
set4.remove(20) # 將 set4 中的 20 刪除

print(set2)
print(set4)


集合可使用的函式
與串列 (List) 和數組 (Tuple) 一樣可以使用以下函式

len() 回傳長度

sum() 回傳總和

max() 回傳最大值

min() 回傳最小值

set1 = {2, 4, 6, 8, 10}

print(len(set1))
print(sum(set1))
print(max(set1))
print(min(set1))


判斷元素是否存在於集合中
與串列 (List) 和數組 (Tuple) 一樣可以使用 in 和 not in 來判斷元素是否存在於集合中

set1 = {2, 4, 6, 8, 10}

print(2 in set1)
print(11 in set1)
print(3 not in set1)
print(4 not in set1)

參考資料：https://wenyuangg.github.io/posts/python3/python-set.html
