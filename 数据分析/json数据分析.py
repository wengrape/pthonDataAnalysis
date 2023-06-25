import pandas as pd

ve={
   "school_name": "湖南机电",
   "location": "长沙",
   "students": [
     {
       "id": ["0001","dds"],
       "name": "张三",
       "sex": "男",
       "age": 20
     },
     {
       "id": "0002",
       "name": "李四",
       "sex": "女",
       "age": 19
     }
   ]
 }



print(pd.read_json("data/simple.json"))
print(pd.json_normalize(ve,record_path=["students"],meta=["school_name"]))

# print("hh:",pd.json_normalize([1,2,3,4,23,12])) 错误
ve1=pd.DataFrame(ve)
ve1.to_json("hj.json")  # encoding="utf-8" bukey

print(pd.read_excel("data/Athletes_info.xlsx",sheet_name=0))




