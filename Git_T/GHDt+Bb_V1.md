# 不用代碼也可以使用 Git

> ~~我亂說的。~~

> 從零開始的 Git 使用教程。
> **GitHub Desktop 與 Bitbucket 篇。**

> Copyright © 2017 undecV.
> [![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
> This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

------

- 在上文（[不用代碼也可以使用 Git 系列之 GitHub Desktop 客戶端篇](GHDt_V1.md)）中，你已經完成了 GitHub Desktop 的設定，也了解的最基本的 Git 操作在 GitHub Desktop 下如何完成。
- 本文將會告訴你，如何在 GitHub Desktop 中，與 Bitbucket 愉快的玩耍。
- Bitbucket 相對於 Github，免費支持最多 5 人的私有版本庫。
- 當然，GitHub Desktop 是由 GitHub 出品，Bitbucket 也有自己的 Git 客戶端叫做 SourceTree。

1. 到 [Bitbucket](https://bitbucket.org/) 註冊賬戶。（我再略！

2. - 在 Bitbucket 網頁中如何創建一個版本庫，在頁面最上方的 `Repositories` 菜單中選擇 `Create repository`，並填入相關的資訊（名字，公開，版本庫的類型，描述，etc...）。
   - 請注意，Bitbucket 除了 Git 之外，還提供另一種版本管理的軟體，但是我們仍然選擇 Git。
   - 請注意，在 Git 中，動作 `Fork` 可以將一個（你不具編輯權限的）版本庫複製一份完全相同的版本庫到你的賬戶下，這樣你對該版本庫就有完全的權限操作。在 `Forking` 選項中，可以選擇是否應許他人 Fork 你的版本庫。
   - ![Options](GHDt+Bb_V1/P_00.png)

3. 設定 GitHub Desktop： 
   - 右上角的 齒輪，然後選擇 Options...。
     - ![Options](GHDt_V1/P_01.png)
   - 設定項目，其中的：
     2. Configure git：你的 Git 配置，要使用 Git 你需要一個全名（`Full name`）和電郵地址（`Email`），請與在註冊 Bitbucket 時所填寫的一致，這樣 Git 才會知道誰提交了編輯。
     - ![Options](GHDt_V1/P_02.png)

- 這樣，你的 GitHub Desktop 就設定完了，
  那麼，該如何在 GitHub Desktop 中，與 Bitbucket 愉快的玩耍呢？
  1. 在你的版本庫列表中，右擊并選擇 `Open in Git Shell`， 打開 Shell（PowerShell 或者 CMD）。
     - ![Options](GHDt+Bb_V1/P_01.png)
  2. 使用 `cd` 指令，回到 Clone path，或者你想要把版本庫放置的地方。
  3. 在你的 Bitbucket 版本庫的頁面中，點擊左邊的 `Clone`，並且複製文字框內的所有內容。
     - ![Options](GHDt+Bb_V1/P_02.png)
  4. 在你的 Shell 中（PowerShell 或者 CMD）中粘貼所有的內容並且執行。
     - 這個指令就是將你的 Bitbucket 版本庫，克隆一份到你指定的目錄下。
  5. 回到 GitHub Desktop 中，點擊左上角的 `+` 號，選擇 `Add` 頁面，並且選擇你剛剛克隆的版本庫所在的目錄。
     - ![Options](GHDt+Bb_V1/P_03.png)
- 之後它就會出現在左邊的版本庫列表中，其他的操作就跟上一個教程差不多了。
- 最後，你已經了解了在 GitHub Desktop 下如何使用 Bitbucket 託管的版本庫。那麼，你也可能感興趣：
  - 不用代碼也可以使用 Git 系列之
    - [GitHub Desktop + GitHub 篇](GHDt+GH_V1.md) 

------

- See also:
- Release Notes:
  - 1.0 Publish (20170302)