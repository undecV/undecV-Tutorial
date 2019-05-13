# 精簡版 Markdown 語法

> Apache HTTP server - Part 番外之一

> Q: 如何快速生成作業要求的 HTML 網頁？

> ~~連猴子都能懂的 Markdown 教程~~

> [![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
> To the extent possible under law, the person who associated CC0 with this work has waived all copyright and related or neighboring rights to this work.

---

> **Markdown** 是一種[輕量級標記式語言](https://zh.wikipedia.org/wiki/轻量级标记语言)，創始人為[約翰·格魯伯](https://zh.wikipedia.org/wiki/約翰·格魯伯)（John Gruber）。它允許人們「使用易讀易寫的純文字格式編寫文件，然後轉換成有效的[XHTML](https://zh.wikipedia.org/wiki/XHTML)（或者[HTML](https://zh.wikipedia.org/wiki/HTML)）文件」。
>
> -- Wikipedia ([CC BY-SA 3.0](https://zh.wikipedia.org/zh-tw/Wikipedia:CC_BY-SA_3.0协议文本))

Markdown 的文件擴展名為`.md` 。

光是這個介紹就很符合作業要求啊，可是我經常拿來轉換成 PDF 就是了ww。

---

> **注意！**
> **並不是所有的 Markdown 編輯器或閱讀器都能完整的包括下述的功能，在不同的編輯器和 CSS Theme 下，顯示的結果可能略有不同。**  

---

- ### 標題
  ```markdown
  # 一級標題
  ## 二級標題
  ### 三級標題
  #### 四級標題
  ##### 五級標題
  ###### 六級標題
  ```
  - 演示：
    - # 一級標題
    - ## 二級標題
    - ### 三級標題
    - #### 四級標題
    - ##### 五級標題
    - ###### 六級標題

- ### 段落
  - 空行分割段落。

- ### 列表
  ```markdown
  - 其一
  - 其一
  - 其一
  ```
  - 演示：
    - 其一
    - 其一
    - 其一

- ### 有序列表
  ```markdown
  1. 其一
  2. 其二
  3. 其三
  ```
  - 演示：
    1. 其一
    2. 其二
    3. 其三

- ### 鏈接、鏈接引用、圖片
  ```markdown
  [Markdown - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/Markdown)
  ```
  - 演示：
    - [Markdown - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/Markdown)
  ```markdown
  [文字][標籤]
  ```
  - 演示：
    - [文字][標籤]
  ```markdown
  [標籤]: 地址 "標題"
  ```
  - 演示：
    - [標籤]: 地址 "標題"
  ```markdown
  ![當圖片無法顯示時顯示這段文字](pic.png)
  [pic]: pic.png
  ```
  - 演示：
    - ![當圖片無法顯示時顯示這段文字][pic.png]
    - [pic]:pic.png
  ```markdown
  文字[^1]
  [^1]: 註腳
  ```
  - 演示：
    - 文字[^1]
    - [^1]: 註腳

- ### 強調
  ```markdown
  *強調* _強調_
  **加重強調** __加重強調__
  <u>底線</u>
  `程式`
  ~~刪除~~
  <!--注釋-->
  ```
  - 演示：
    - *強調* _強調_
    - **加重強調** __加重強調__
    - <u>底線</u>
    - `程式`
    - ~~刪除~~
    - <!--注釋-->
- ### 數學
  ```markdown
  $1+1 = 2$

  $$
  2+2 = 4
  $$
  ```
  - 演示：
    - $1+1 = 2$
    - $$
      2+2 = 4
      $$

- ### 表格
  ```markdown
  | T1   |  T2  |   T3 |
  | :--- | :--: | ---: |
  | C1R1 | C2R1 | C3R1 |
  | C2R1 | C2R2 | C3R2 |
  ```
  - 演示：
    | T1   |  T2  |   T3 |
    | :--- | :--: | ---: |
    | C1R1 | C2R1 | C3R1 |
    | C2R1 | C2R2 | C3R2 |
- ### 參照
  ```markdown
  > 參照

  > 第一層
  > 
  > > 第二層
  > 
  > 第一層
  ```
- 演示：
  > 參照

  > 第一層
  >
  > > 第二層
  >
  > 第一層
- ### 分割線
  ```markdown
  ---
  ***
  -----
  *****
  ```
  - 演示：
    - ---
    - ***
    - -----
    - *****

- ### 程式碼
  > 使用三個反引號 ` ``` ` 。
  - 演示：
    ```c++
    #include <iostream>
    using namespace std;
    int main(int argc, char *argv[]){
        printf("Hello World!");
        system("pause");
        return 0;
    }
    ```

---

- See Also:
  - > Markdown - Wikipedia
    > https://en.wikipedia.org/wiki/Markdown

  - > Markdown | GitBook 中文解說 - 2.4
    > https://wastemobile.gitbooks.io/gitbook-chinese/content/format/markdown.html

- Release Notes:

  - 2.0 Update (20170301):
    - 變更授權：`CC0` 。
    - 細節修正。
    - 內容整合。
