import pandas as pd
# import splite3   #pandas唯一支持的数据库




file = 'E:/2345Downloads/melb_data.csv'
file1 = 'E:/2345Downloads/xls-files-all/WICAgencies2013ytd.xls'

# df = pd.read_csv(file)
df = pd.read_excel(file1)
# tables = pd.read_sql_query("SELECT * FROM sqlite_master where type='table'", con)
# print(tables)
print(df.shape)

pd.set_option("max_rows",10)
print(df)