import pandas as pd

'''
data = {
    'name': ['W', 'C', 'L', 'D'],
    'email': ['min@gmail.com', 'hchang@gmail.com', 'laioding@gmail.com', 'hsulight@gmail.com'],
    'grades': [60, 77, 92, 43]
}

# 建立 DataFrame 物件
student_df = pd.DataFrame(data)

# 將 DataFrame 轉成 CSV 檔案
print(student_df.to_csv('student_demo.csv'))
'''
import csv
import numpy as np
if __name__ == "__main__":
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--training", default="training_data.csv", help="input training data file name")
    parser.add_argument("--testing", default="testing_data.csv", help="input testing data file name")
    parser.add_argument("--output", default="output.csv", help="output file name")
    args = parser.parse_args()

    # The following part is an example.
    # You can modify it at will.
iCount = 0
iCount_ForLoop = 0  # 總計抓了幾筆的trainingData   1年或是半年
fTotal = 0.0;
fAvg = 0.0  # 均線
List = [0]  # 計畫行為  第一天先買進
istock = 0  # 目前的庫藏

fcloseStock_Today = 0.0
fcloseStock_Yesday = 0.0  # 昨日
iSTs = 0  # 連續2天情勢

# 讀入training_data
path = 'training_data.csv'
with open(path, newline='', encoding="utf-8") as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    # data = np.asarray(list(rows))
    for row in rows:
        fTotal = fTotal + float(row[3])
        # if float(row[3]) > 50:
        # print(row)
        if (iCount_ForLoop) > 179:
            break
        iCount_ForLoop = iCount_ForLoop + 1  # 只抓半年的資料量

    # print(iCount_ForLoop)

fAvg = fTotal / iCount_ForLoop
print(fAvg)

# 輸入test_Data
path = 'testing_data.csv'
with open(path, newline='', encoding="utf-8") as csvfile1:
    rows = csv.reader(csvfile1, delimiter=',')
    # data = np.asarray(list(rows))
    for row in rows:
        # 第一天及 最後一天不計
        if (iCount == 0 or iCount == 19):
            print('continue')
            iCount = iCount + 1
            continue
        fcloseStock_Today = float(row[3])  # 只看收盤價
        if fcloseStock_Today > fcloseStock_Yesday and istock < 1 and iSTs < 2:    #收盤價連續漲2天 且 可買進
            istock = istock + 1
            iSTs = iSTs + 1
            List.append(1)
        elif fcloseStock_Today < fcloseStock_Yesday and istock > -1 and iSTs < 2:  #收盤價連續跌2天 且 可以賣出
            istock = istock - 1
            iSTs = iSTs - 1
            List.append(-1)
        else:
            List.append(0)
        # print(row[3])
        print('庫藏股:' + str(istock))
        print(List)
        fcloseStock_Yesday = fcloseStock_Today
        iCount = iCount + 1

# 產生output
with open('output.csv', 'w', newline='', encoding="utf-8") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    Test = List[2]
    # writer.writerow(str(Test))
    # print(Test)
    for i in range(0, 19):
        # writer.writerow([a])
        # writer.writerow('a')
        # print(Test)
        writer.writerow(str(List[i]))

