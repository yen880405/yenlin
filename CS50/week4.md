# Merge sort
合併排序（英語：Merge sort，或mergesort），是建立在合併操作上的一種有效的排序演算法，效率為O(n\log n)（大O符號）。
1945年由約翰·馮·紐曼首次提出。該演算法是採用分治法（Divide and Conquer）的一個非常典型的應用，且各層分治遞迴可以同時進行。</br>
 <img src='https://github.com/yen880405/yenlin/blob/master/image/merge-sort.png'></br>
演算法分為以下三步驟：
(1)將含有 n 個元素的序列分割成含有 n / 2 個子序列
(2)排序分割後的兩個子序列
(3)合併排序完成的兩子序列，成為一個排好序的序列
* BEST:Ο(n log n)
* WORST:Ο(n log n)
* AVERAGE:Ο(n log n)


# 遞迴（Recursion）

遞迴（英語：Recursion），又譯為遞歸，在數學與電腦科學中，是指在函數的定義中使用函數自身的方法。遞迴一詞還較常用於描述以自相似方法重複事物的過程。例如，當兩面鏡子相互之間近似平行時，
鏡中巢狀的圖像是以無限遞迴的形式出現的。也可以理解為自我複製的過程。

小心得：
這次的merge sort是個廣受大眾歡迎的演算法，普遍被大眾運用，所以蔡老師的課程與此相當符合，是極須掌握得一個演算法，
然而，遞迴如同while 和for， 使這個程式碼有個迴圈遞迴，加速演算數率。

參考資料：https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92
