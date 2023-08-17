import xml.etree.ElementTree as ET
#匯入xml函示庫 並且命名為ET
def xml_to_dict(element):
    result={}
    for child in element:
        if len(child)==0:
            result[child.tag]=child.text
        else:
            result[child.tag]=xml_to_dict(child)
    return result

tree=ET.parse("setting.xml")#讀取設定檔
root=tree.getroot()#獲取裡面的資料
data=xml_to_dict(root)#把資料轉化為dictionary處理
money=int(data["money"])
interest=int(data["interest"])
month=int(data["month"])
total=0
for i in range(month):
    total=total+money
    total=total*(1+interest/100)
result=open("result.txt","w",encoding="utf-8")#建立儲存最終數據的檔案
result.write("你最後剩下的錢為:"+str(int(total)))#寫入數據
result.close()#關閉檔案
print(int(total))#輸出總金額