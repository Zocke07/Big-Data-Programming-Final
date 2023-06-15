### Import By Year
#### For the full code, you can see here: https://github.com/Zocke07/Big-Data-Programming-Final/blob/main/ImportByYear/ImportsByYear.py
Here are the brief explanations of the code: 
```
import chardet
import pandas as pd
import matplotlib.pyplot as plt
```
The code imports the necessary libraries: chardet for character encoding detection, pandas for data manipulation and analysis, and matplotlib.pyplot for data visualization.  
```
with open('u2010im.csv', 'rb') as file:
    result = chardet.detect(file.read())
```
This block of code opens the file 'u2010im.csv' in binary mode ('rb'). It then reads the file contents and uses the chardet.detect() function to detect the character encoding of the file. The detected encoding is stored in the result variable.  
```
data = pd.read_csv('u2010im.csv', encoding=result['encoding'])
data1 = data
```
These lines read the CSV file 'u2010im.csv' into a pandas DataFrame called data. The encoding parameter is set to result['encoding'], which is the detected encoding from the previous step. This ensures that the file is read correctly. The DataFrame data is then assigned to data1, creating a copy.  
```
year = []
total = []
print("Year", " ", "Imports from Country (Unit : US$ Thousand)")
for i, j in data1.groupby('Imports from Country (Unit : US$ Thousand)')['總計'].sum().iteritems():
    if '月' in i:
        continue
    year.append(i)
    total.append(j)
    print(i, j)
```
This section initializes empty lists year and total to store the year and total import values respectively. The print statement outputs a header for the data to be displayed.  
The for loop iterates over the grouped data in the DataFrame data1. It groups the data based on the column 'Imports from Country (Unit : US$ Thousand)' and calculates the sum of the column '總計' for each group (presumably representing the total imports from each country for a specific year). The iteritems() method is used to retrieve the index (year) and the corresponding sum (total imports) for each group.  
If the index (i) contains the character '月' (representing a month), the iteration continues to the next item. Otherwise, the year and total imports are appended to the respective lists (year and total), and the values are printed.  
```
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(year, total)
ax.set_xticklabels(year, rotation='vertical')
ax.ticklabel_format(style='plain', axis='y')
plt.title("Import Trade Value")
plt.xlabel("Year")
plt.ylabel("Imports from Country (Unit : US$ Thousand)")
plt.show()
```
This block of code creates a figure and axis object for the plot using plt.subplots(). The figsize parameter is set to (10, 6) pixels to define the size of the plot.  
The ax.bar() function is used to create a bar plot. The year list is used as the x-axis values, and the total list is used as the corresponding bar heights.  
The ax.set_xticklabels() function sets the x-axis tick labels to be the values from the year list. The rotation parameter is set to 'vertical' to display the labels vertically.  
The ax.ticklabel_format() function is used to format the y-axis tick labels to be displayed in plain style (without scientific notation).  
Finally, the plot title, x-axis label, and y-axis label are set using plt.title(), plt.xlabel(), and plt.ylabel() respectively.  
The plot is displayed using plt.show().  
