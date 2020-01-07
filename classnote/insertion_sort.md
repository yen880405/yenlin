# 簡介

Insertion Sort(插入排序法)
想像手上有一副撲克牌，若想要將紙牌從左到右按照「小到大」排序。

Insertion Sort的方法為：將第i張紙牌加入「前i−1張排序過」的紙牌組合，得到i張排序過的紙牌組合。

以圖一為例，從左邊數來的前三張紙牌已經排好序：index(0)、index(1)、index(2)分別為1、3、5，現在要將第四張紙牌(index(3)，數值為2)加入前三張牌，想要得到「前四張排好序」的紙牌組合。
經由觀察，最終結果的紙牌順序為1、2、3、5，可以透過以下步驟完成：

原先index(2)的5搬到index(3)；
原先index(1)的3搬到index(2)；
原先index(3)的2搬到index(1)；
如此便能把第4張紙牌加入(insert)「前3張排序過」的紙牌組合，得到「前4張排序過」的紙牌組合。

<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.19.14.png'>

由以上說明可以看出，Insertion Sort要求，在處理第i筆資料時，第1筆至第i−1筆資料必須先排好序。
那麼，只要按照順序，從第1筆資料開始處理，便能確保「處理第2筆資料時，第1筆資料已經排好序」，「處理第3筆資料時，第1筆、第2筆資料已經排好序」，依此類推，若共有N筆資料，必定能夠在處理第N筆資料時，將第1筆至第N−1筆資料排序過。
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.21.28.png'>
# 圖解邏輯
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.23.08.png'>

參考資料：http://alrightchiu.github.io/SecondRound/comparison-sort-insertion-sortcha-ru-pai-xu-fa.html

