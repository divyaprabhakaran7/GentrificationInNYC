import os
import pandas as pd

demographics = pd.DataFrame()

brooklyn_xlsx = [f for f in os.listdir("BK/") if f[-4:] == 'xlsx']
brooklyn = pd.DataFrame()
bronx_xlsx = [f for f in os.listdir("BX/") if f[-4:] == 'xlsx']
bronx = pd.DataFrame()
man_xlsx = [f for f in os.listdir("MN/") if f[-4:] == 'xlsx']
manhattan = pd.DataFrame()
queens_xlsx = [f for f in os.listdir("QN/") if f[-4:] == 'xlsx']
queens = pd.DataFrame()
si_xlsx = [f for f in os.listdir("SI/") if f[-4:] == 'xlsx']
statisl = pd.DataFrame()

# Brooklyn files
for file in brooklyn_xlsx:
    data = pd.ExcelFile("BK/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    brooklyn = brooklyn.append(sheet2)
    
bk_asian = brooklyn[brooklyn["Indicator"] == "Percent Asian"]
bk_black = brooklyn[brooklyn["Indicator"] == "Percent black"]
bk_hispanic = brooklyn[brooklyn["Indicator"] == "Percent Hispanic"]
bk_white = brooklyn[brooklyn["Indicator"] == "Percent white"]

demographics = demographics.append([bk_asian, bk_black, bk_hispanic, bk_white])

# Bronx files
for file in bronx_xlsx:
    data = pd.ExcelFile("BX/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    bronx = bronx.append(sheet2)
    
bx_asian = bronx[bronx["Indicator"] == "Percent Asian"]
bx_black = bronx[bronx["Indicator"] == "Percent black"]
bx_hispanic = bronx[bronx["Indicator"] == "Percent Hispanic"]
bx_white = bronx[bronx["Indicator"] == "Percent white"]

demographics = demographics.append([bx_asian, bx_black, bx_hispanic, bx_white])

# Manhattan files
for file in man_xlsx:
    data = pd.ExcelFile("MN/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    manhattan = manhattan.append(sheet2)
    
mn_asian = manhattan[manhattan["Indicator"] == "Percent Asian"]
mn_black = manhattan[manhattan["Indicator"] == "Percent black"]
mn_hispanic = manhattan[manhattan["Indicator"] == "Percent Hispanic"]
mn_white = manhattan[manhattan["Indicator"] == "Percent white"]

demographics = demographics.append([mn_asian, mn_black, mn_hispanic, mn_white])

# Queens files
for file in queens_xlsx:
    data = pd.ExcelFile("QN/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    queens = queens.append(sheet2)
    
qn_asian = queens[queens["Indicator"] == "Percent Asian"]
qn_black = queens[queens["Indicator"] == "Percent black"]
qn_hispanic = queens[queens["Indicator"] == "Percent Hispanic"]
qn_white = queens[queens["Indicator"] == "Percent white"]

demographics = demographics.append([qn_asian, qn_black, qn_hispanic, qn_white])

# Staten Island files
for file in si_xlsx:
    data = pd.ExcelFile("SI/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    statisl = statisl.append(sheet2)
    
si_asian = statisl[statisl["Indicator"] == "Percent Asian"]
si_black = queens[statisl["Indicator"] == "Percent black"]
si_hispanic = statisl[statisl["Indicator"] == "Percent Hispanic"]
si_white = statisl[statisl["Indicator"] == "Percent white"]

demographics = demographics.append([si_asian, si_black, si_hispanic, si_white])

percent_white = pd.DataFrame()
percent_white = percent_white.append([bk_white, bx_white, mn_white, qn_white, si_white])

cols = [1,2,3,4,10,11,12,13] #columns irrelevant to analysis
percent_white = percent_white.drop(percent_white.columns[cols],axis=1) #removing irrelevant columns


import matplotlib.pyplot as plt
import itertools

years = [2000, 2006, 2010, 2017, 2018]

no_indices = percent_white.to_string(index=False)
title = '\033[1m' + "Percentage White by Community Board Over Time"+'\033[0m'
print(title.center(70))
print(no_indices)

colors = itertools.cycle(["red", "orange", "yellow", "lightgreen", "green", "turquoise", "lightblue", "blue", "navy", "violet", "purple", "pink", "deeppink", "gray", "maroon"])
                
for index,row in percent_white.iterrows():
    name = row["Community District"]
    values = [row[2000], row[2006], row[2010], row[2017], row[2018]]
    values = [float(x.strip('%')) for x in values]
   
    plt.plot(years, values, marker='o',c=next(colors), label = name)
    plt.legend(bbox_to_anchor=(1.05,1), title="Community Board")
    
    plt.ylim(0,100)
    plt.xticks(years, ['2000', '2006', '2010', '2017', '2018'])
    plt.ylabel("Percent")
    plt.xlabel("Year")
    plt.title("Percentage of White Residents by Community Board Over Time")

plt.show()
