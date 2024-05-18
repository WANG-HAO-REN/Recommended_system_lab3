import pandas as pd

each_year_result = []
for year in range(103,109) :
    csv_name =  "{}_student.csv".format(year)
    df = pd.read_csv(csv_name)

    df = df[['學校名稱','一年級男生','一年級女生','二年級男生','二年級女生','三年級男生','三年級女生','四年級男生','四年級女生','五年級男生','五年級女生','六年級男生','六年級女生','七年級男生','七年級女生','延修生男生','延修生女生']]
    # 將人數 - 轉換為 0
    # df.replace('-', 0, inplace=True)
    # 將所有列轉換為數字， "1,055" => 1055  coerce 無法轉換的變為 NaN， (fillna(0) NaN 轉換為 0)
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    total_filed_name = "{}_total_stu".format(year)
    # 人數相加 (橫)
    df[total_filed_name] = df.iloc[:, 1:].sum(axis=1)
    # 人數相加 (直 by 學校名稱 ) 
    each_year_result = df.groupby('學校名稱')[total_filed_name].sum()
    #依照學校名稱 合併結果
    if year == 103 :
        result = each_year_result
    else :
        result = pd.merge(result, each_year_result, on='學校名稱', how='outer') ; #outer 聯集 不存在為NaN

print(result)