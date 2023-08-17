# codingbar.money# 定期定額獲利計算器

這是一個簡單的程式，用於計算定期定額方式投資的獲利，並將結果儲存到檔案中。該程式使用 Python 語言編寫，使用 `xml.etree.ElementTree` 模組來解析 XML 配置檔案。

## 如何使用

** 準備設定檔案：**

在程式運行之前，請創建一個名為 `setting.xml` 的 XML 設定檔。在這個檔案中，您可以指定投資的金額、年利率和投資期數。以下是一個範例的 `setting.xml` 配置：

```xml
<data>
   <money>10000</money>
   <interest>12</interest>
   <month>36</month>
</data>


## 運行程式：

使用 Python 運行 main.py 程式。程式將讀取 setting.xml 配置檔案，計算定期定額投資的獲利，然後將結果儲存到 result.txt 檔案中。同時，也會在終端輸出計算結果。

## 查看計算結果：

運行程式後，您將在終端和 result.txt 檔案中看到計算結果。result.txt 檔案將包含您最後剩下的金額。

## 程式概述 :
main.py：主要的程式檔案，包含了程式的執行邏輯和主要計算過程。

setting.xml：XML 配置檔，包含了投資的相關設定，如每期投資金額、預期年利率和投資期數。

xml_to_dict 函式：這個函式將 XML 元素轉換為 Python 字典，方便後續程式使用。

result.txt：程式執行後生成的檔案，包含了計算結果。

## 注意事項
這個程式的計算結果是基於提供的資訊進行估算的，實際獲利可能會有所不同。

請確保 setting.xml 配置檔案存在並包含正確的設定資訊，否則程式可能會出錯。

此程式僅供學習和測試用途，不保證特定的投資結果。
