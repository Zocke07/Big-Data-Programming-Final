import chardet
import pandas as pd
import matplotlib.pyplot as plt

with open('u2010im.csv', 'rb') as file:
    result = chardet.detect(file.read())

plt.rcParams["font.sans-serif"] = "DFKai-SB"
plt.rcParams["axes.unicode_minus"] = False

data = pd.read_csv('u2010im.csv', encoding=result['encoding'])
data1 = data

country_index = 0
year_index = 273

countries = data.columns
values = data.iloc[year_index]

result = list(zip(countries, values))

for item in result:
    for i in item:
        if '洲' in str(i):
            result.remove(item)

sorted_list = sorted(result[2:], key=lambda x: x[1], reverse=True)

topCountries = []
theValues = []

for n in range(10):
    topCountries.append(sorted_list[n][0])
    theValues.append(sorted_list[n][1])
    
def htmlTable():
    theTable = '<table border = 1>\n'
    theTable += '<tr>\n'
    theTable += '<td>Countries</td>\n'
    theTable += '<td>Imports from Country</td>\n'
    theTable += '</tr>\n'
    for row in range(len(topCountries)):
        theTable += '<tr>\n'
        theTable += f'<td>{topCountries[row]}</td>\n'
        theTable += f'<td>{theValues[row]}</td>\n'
        theTable += '</tr>\n'
    theTable += '</table>'
    return theTable

tableResult = htmlTable()

f = open("TableByCountry.html", "w", encoding='utf-8')
f.write(tableResult)
f.close()

fig, ax = plt.subplots(figsize=(10, 6))
plt.title("Import Trade Value")
plt.xlabel("Countries")
plt.ylabel("Imports from Country (Unit : US$ Thousand)")
ax.set_xticklabels(topCountries)
ax.ticklabel_format(style='plain', axis='y')
plt.plot(topCountries, theValues)
plt.show()
