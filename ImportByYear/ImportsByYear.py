import chardet
import pandas as pd
import matplotlib.pyplot as plt

with open('u2010im.csv', 'rb') as file:
    result = chardet.detect(file.read())

plt.rcParams["font.sans-serif"] = "DFKai-SB"
plt.rcParams["axes.unicode_minus"] = False

data = pd.read_csv('u2010im.csv', encoding=result['encoding'])
data1 = data
year = []
total = []
print("Year", " ", "Imports from Country (Unit : US$ Thousand)")
for i, j in data1.groupby('Imports from Country (Unit : US$ Thousand)')['總計'].sum().iteritems():
    if '月' in i:
        continue
    year.append(i)
    total.append(j)
    print(i, j)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(year, total)
ax.set_xticklabels(year, rotation='vertical')
ax.ticklabel_format(style='plain', axis='y')
plt.title("Import Trade Value")
plt.xlabel("Year")
plt.ylabel("Imports from Country (Unit : US$ Thousand)")
plt.show()
