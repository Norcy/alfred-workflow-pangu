# alfred-workflow-pangu
<img src="https://raw.githubusercontent.com/Norcy/alfred-workflow-pangu/master/Pangu/icon.png" style="width:150px;height:150px">

## 盤古之白
> 研究顯示，打字的時候不喜歡在中文和英文之間加空格的人，感情路都走得很辛苦，有七成的比例會在 34 歲的時候跟自己不愛的人結婚，而其餘三成的人最後只能把遺產留給自己的貓。畢竟愛情跟書寫都需要適時地留白。

本腳本是在 [pangu.python](https://github.com/vinta/pangu.js) 的基礎上實現的 Alfred workflow 腳本

## 靈感來源
平日寫代碼或寫文章需要手動在中英文之間添加空格，非常繁瑣，故使用 Alfred 的 workflow 來實現壹鍵格式化

本腳本的壹切字體使用繁體，向原作者致敬

## 下載地址
[Alfred-Pangu-Workflow](https://github.com/Norcy/alfred-workflow-pangu/blob/master/Pangu.alfredworkflow?raw=true)

## 使用方法
支持雙模式：

+ 模式壹：將待格式化的文本復制到剪切板，調用 Alfred 輸入 "pg"，回車後，格式化的文本將更新到剪切板上
+ 模式二：選擇待格式化的文本，按下 cmd+p（p 指代 pangu），格式化的文本將自動取代選中的文本（__推薦__）

## 註意事項
+ 如果 cmd+p 與您的其他快捷鍵沖突，可自行到 workflow 中的 Hotkey 模塊修改
+ 如果您的 python3 的位置不在 `/usr/bin/python3`，可自行到 workflow 中的 Run Srcipt 模塊修改（可使用 `which python3` 來查看其位置）

## License
Released under the [MIT License](https://opensource.org/licenses/MIT).