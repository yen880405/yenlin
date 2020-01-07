https://markdown.tw/#p  </br>
這個網址內容很實用又簡單明瞭推薦給大家
裡面的東西相當實用，大部分的資訊功能都有，在這裡簡單簡介一下

# 概述功能

段落和換行
一個段落是由一個以上相連接的行句組成，而一個以上的空行則會切分出不同的段落（空行的定義是顯示上看起來像是空行，便會被視為空行。比方說，若某一行只包含空白和tab，則該行也會被視為空行），一般的段落不需要用空白或斷行縮排。

「一個以上相連接的行句組成」這句話其實暗示了Markdown允許段落內的強迫斷行，這個特性和其他大部分的text-to-HTML格式不一樣（包括 MovableType的「Convert Line Breaks」選項），其他的格式會把每個斷行都轉成<br />標籤。

如果你真的想要插入<br />標籤的話，在行尾加上兩個以上的空白，然後按enter。

是的，這確實需要花比較多功夫來插入<br />，但是「每個換行都轉換為<br />」的方法在Markdown中並不適合， Markdown中email式的區塊引言和多段落的清單在使用換行來排版的時候，不但更好用，還更好閱讀。

標題
Markdown支援兩種標題的語法，Setext和atx形式。

Setext形式是用底線的形式，利用=（最高階標題）和-（第二階標題），例如：

This is an H1
=============

This is an H2
-------------
任何數量的=和-都可以有效果。

Atx形式則是在行首插入1到6個 # ，各對應到標題1到6階，例如：

# This is an H1

## This is an H2

###### This is an H6
你可以選擇性地「關閉」atx樣式的標題，這純粹只是美觀用的，若是覺得這樣看起來比較舒適，你就可以在行尾加上#，而行尾的#數量也不用和開頭一樣（行首的井字數量決定標題的階數）：

# This is an H1 #

## This is an H2 ##

### This is an H3 ######

清單
Markdown支援有序清單和無序清單。

無序清單使用星號、加號或是減號作為清單標記：

*   Red
*   Green
*   Blue
等同於：

+   Red
+   Green
+   Blue
也等同於：

-   Red
-   Green
-   Blue
有序清單則使用數字接著一個英文句點：

1.  Bird
2.  McHale
3.  Parish
很重要的一點是，你在清單標記上使用的數字並不會影響輸出的HTML結果，上面的清單所產生的HTML標記為：

<ol>
<li>Bird</li>
<li>McHale</li>
<li>Parish</li>
</ol>

分隔線
你可以在一行中用三個或以上的星號、減號、底線來建立一個分隔線，行內不能有其他東西。你也可以在星號中間插入空白。下面每種寫法都可以建立分隔線：



---------------------------------------

參考資料：https://markdown.tw/#p