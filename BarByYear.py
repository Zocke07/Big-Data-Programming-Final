import csv
import chardet
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Detect the encoding of the file
with open('u2010im.csv', 'rb') as file:
    result = chardet.detect(file.read())

# Read the file with the detected encoding
data = pd.read_csv('u2010im.csv', encoding=result['encoding'])
data1 = data
year = []
total = []
for i, j in data1.groupby('Imports from Country (Unit : US$ Thousand)')['總計'].sum().iteritems():
    if '月' in i:
        continue
    year.append(i)
    total.append(j)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(year, total)
ax.set_xticklabels(year, rotation='vertical')
ax.ticklabel_format(style='plain', axis='y')
plt.title("Import Trade Value")
plt.xlabel("Imports from Country (Unit : US$ Thousand)")
plt.ylabel("總計")
plt.show()

ax.pie(total, labels=year, autopct='%1.1f%%')
plt.show()
