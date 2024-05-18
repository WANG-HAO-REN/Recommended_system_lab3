import pandas as pd

df=pd.DataFrame()
dict_stu = dict()
list_stu = [x for x in range(6,22)]
list_stu = [1] +list_stu

for x in range(103,104) :
    url="https://stats.moe.gov.tw/files/detail/"+str(x)+"/"+str(x)+"_student.csv"
      # "https://stats.moe.gov.tw/files/detail/103/103_student.csv"
    print(url)
    data = pd.read_csv(url, usecols= list_stu)
    break
    for col in data.columns[1:]:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
    for i in range(1, data.shape[0]):
        data[str(x)+"_total_stu"] = data.iloc[i][2:17].sum()
    print(data[['學校名稱', str(x)+"_total_stu"]])

# print(result)