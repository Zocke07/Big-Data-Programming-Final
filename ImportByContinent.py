import chardet
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def getNum(continent, country_lst):
    num = 0
    for i in country_lst:
        for j in continent:
            if i==j:
                num+=1
                break
    return num

def getTitle(data):
    title=[]
    headers = data.columns
    for header in headers:
        title.append(header)
    return title

def findCountry(url,num):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the table containing the data
    table = soup.find("table", class_="wikitable sortable")
    
    # Extract the country name column
    country = []
    for row in table.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) > num:
            name_column=columns[num].text.strip()
            temp = 0
            for i in name_column:
                if (i =='[') or (i == '（') or (i=='(') or (i =='、'):
                    country.append(name_column.split(i)[0])
                    break
                if temp == len(name_column)-1:
                    country.append(name_column)
                temp += 1
    return country

Africa = findCountry("https://zh.wikipedia.org/zh-tw/%E9%9D%9E%E6%B4%B2%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E5%88%97%E8%A1%A8",0)
Asia = findCountry("https://zh.wikipedia.org/zh-tw/%E4%BA%9A%E6%B4%B2%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E5%88%97%E8%A1%A8",1)
Europe = findCountry("https://zh.wikipedia.org/zh-tw/%E6%AD%90%E6%B4%B2%E5%9C%8B%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8D%80%E5%88%97%E8%A1%A8",1)
N_America = findCountry("https://zh.wikipedia.org/zh-tw/%E5%8C%97%E7%BE%8E%E6%B4%B2%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E5%88%97%E8%A1%A8",1)
S_America = findCountry("https://zh.wikipedia.org/zh-tw/%E5%8D%97%E7%BE%8E%E6%B4%B2%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E5%88%97%E8%A1%A8",1)
Australia = findCountry("https://zh.wikipedia.org/zh-tw/%E5%A4%A7%E6%B4%8B%E6%B4%B2%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E5%88%97%E8%A1%A8",1)
Antarctica = findCountry("https://zh.wikipedia.org/zh-tw/%E5%8D%97%E6%9E%81%E6%B4%B2",0)

# Detect the encoding of the file
with open('u2010im.csv', 'rb') as file:
    result = chardet.detect(file.read())

# Read the file with the detected encoding
data = pd.read_csv('u2010im.csv', encoding=result['encoding'])
title = getTitle(data)
country_lst = title[2:]
continent_lst_str = ['Africa','Asia','Europe','North America','South America','Australia','Antarctica']
continent_lst = [Africa,Asia,Europe,N_America,S_America,Australia,Antarctica]
num = []
for continent in continent_lst:
    num.append(getNum(continent,country_lst))

explode = [0,0,0,0.2,0.2,0.2,0.2]
listm = num
listx = continent_lst_str
plt.title('Import Rate Based on Continent', fontsize=16)
plt.pie(listm, labels = listx, autopct='%2.2f%%',explode=explode)