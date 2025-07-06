import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\Student\Downloads\cricket_data.csv")
print('Cricket data information:', data)
print(' ')
print(data.info())
print(' ')
print('Mean runs scored of every player')

for index,row in data.iterrows():
    print(row["Player_Name"],row["Runs_Scored"])

plt.figure(figsize=(12, 8))
plt.hist(data=data, x='Runs_Scored', bins=20)
plt.title('Distribution of Runs Scored')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(data=data, x='Year', y='Runs_Scored')
plt.title('Trend of Runs Scored Over Years')
plt.xlabel('Year')
plt.ylabel('Runs Scored')
plt.show()


plt.hist(data['Runs_Scored'], bins=20)
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.title('Histogram of Runs Scored')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Runs_Scored'], bins=20, color='orange', edgecolor='black')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.title('Distribution of Runs Scored')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['Centuries'], data['Runs_Scored'], alpha=0.5, color='skyblue')
plt.xlabel('Centuries')
plt.ylabel('Runs Scored')
plt.title('Centuries vs. Runs Scored')
plt.show()



