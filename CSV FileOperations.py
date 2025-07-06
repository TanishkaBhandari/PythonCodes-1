import pandas as pd
tb=pd.read_csv(r"C:\Users\Student\Desktop\myfile.csv")
print('Full file:')
print(tb)
print(' ')
print('Fill NULL places')
print(tb.fillna(5))
print('Remove NULL:')
print(tb.dropna())
print(' ')
for index,row in tb.iterrows():
    print(row["name"],row["marks"])
tb['marks']=[8,9,10,7]
print(tb)
