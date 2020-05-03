import os
import pandas as pd

demographics = pd.DataFrame()
training = pd.DataFrame()


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
#Training data folder
brooklynt_xlsx = [f for f in os.listdir("BKT/") if f[-4:] == 'xlsx']
brooklynt = pd.DataFrame()
bronxt_xlsx = [f for f in os.listdir("BXT/") if f[-4:] == 'xlsx']
bronxt = pd.DataFrame()
mant_xlsx = [f for f in os.listdir("MNT/") if f[-4:] == 'xlsx']
mant = pd.DataFrame()


# Brooklyn files
for file in brooklyn_xlsx:
    data = pd.ExcelFile("BK/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    brooklyn = brooklyn.append(sheet2)
    
bk_asian = brooklyn[brooklyn["Indicator"] == "Percent Asian"]

bk_black = brooklyn[brooklyn["Indicator"] == "Percent black"]
bk_hispanic = brooklyn[brooklyn["Indicator"] == "Percent Hispanic"]
bk_white = brooklyn[brooklyn["Indicator"] == "Percent white"]
#Poverty rate
bk_poverty = brooklyn[brooklyn["Indicator"] == "Poverty rate"]
#Household income
bk_income = brooklyn[brooklyn["Indicator"] == "Median household income (2018$)"]

#Units authorized by new building permits
bk_permits = brooklyn[brooklyn["Indicator"] == "Units authorized by new residential building permits"]

demographics = demographics.append([bk_asian, bk_black, bk_hispanic, 
    bk_white, bk_poverty, bk_income, bk_permits])
#Brooklyn Training Data
for file in brooklynt_xlsx:
    data = pd.ExcelFile("BKT/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    brooklynt = brooklynt.append(sheet2)
    
bkt_asian = brooklynt[brooklynt["Indicator"] == "Percent Asian"]

bkt_black = brooklynt[brooklynt["Indicator"] == "Percent black"]

bkt_hispanic = brooklynt[brooklynt["Indicator"] == "Percent Hispanic"]
bkt_white = brooklynt[brooklynt["Indicator"] == "Percent white"]
#Poverty rate
bkt_poverty = brooklynt[brooklynt["Indicator"] == "Poverty rate"]

#Household income
bkt_income = brooklynt[brooklynt["Indicator"] == "Median household income (2018$)"]
#Units authorized by new building permits
bkt_permits = brooklynt[brooklynt["Indicator"] == "Units authorized by new residential building permits"]

training = training.append([bkt_asian, bkt_black, bkt_hispanic, 
    bkt_white, bkt_poverty, bkt_income, bkt_permits])




# Bronx files
for file in bronx_xlsx:
    data = pd.ExcelFile("BX/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    bronx = bronx.append(sheet2)
    
bx_asian = bronx[bronx["Indicator"] == "Percent Asian"]
bx_black = bronx[bronx["Indicator"] == "Percent black"]
bx_hispanic = bronx[bronx["Indicator"] == "Percent Hispanic"]
bx_white = bronx[bronx["Indicator"] == "Percent white"]


bx_poverty = bronx[bronx["Indicator"] == "Poverty rate"]
bx_income = bronx[bronx["Indicator"] == "Median household income (2018$)"]
bx_permits = bronx[bronx["Indicator"] == "Units authorized by new residential building permits"]

demographics = demographics.append([bx_asian, bx_black, bx_hispanic, bx_white, 
    bx_poverty, bx_income, bx_permits])
#Bronx Training Data
for file in bronxt_xlsx:
    data = pd.ExcelFile("BXT/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    bronxt = bronxt.append(sheet2)
    
bxt_asian = bronxt[bronxt["Indicator"] == "Percent Asian"]

bxt_black = bronxt[bronxt["Indicator"] == "Percent black"]

bxt_hispanic = bronxt[bronxt["Indicator"] == "Percent Hispanic"]
bxt_white = bronxt[bronxt["Indicator"] == "Percent white"]
#Poverty rate
bxt_poverty = bronxt[bronxt["Indicator"] == "Poverty rate"]

#Household income
bxt_income = bronxt[bronxt["Indicator"] == "Median household income (2018$)"]
#Units authorized by new building permits
bxt_permits = bronxt[bronxt["Indicator"] == "Units authorized by new residential building permits"]

training = training.append([bxt_asian, bxt_black, bxt_hispanic, 
    bxt_white, bxt_poverty, bxt_income, bxt_permits])

# Manhattan files
for file in man_xlsx:
    data = pd.ExcelFile("MN/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    manhattan = manhattan.append(sheet2)
    
mn_asian = manhattan[manhattan["Indicator"] == "Percent Asian"]
mn_black = manhattan[manhattan["Indicator"] == "Percent black"]
mn_hispanic = manhattan[manhattan["Indicator"] == "Percent Hispanic"]
mn_white = manhattan[manhattan["Indicator"] == "Percent white"]

mn_poverty = manhattan[manhattan["Indicator"] == "Poverty rate"]
mn_income = manhattan[manhattan["Indicator"] == "Median household income (2018$)"]
mn_permits = manhattan[manhattan["Indicator"] == "Units authorized by new residential building permits"]

demographics = demographics.append([mn_asian, mn_black, mn_hispanic, mn_white, mn_poverty,mn_income, mn_permits])
#Brooklyn Training Data
for file in mant_xlsx:
    data = pd.ExcelFile("MNT/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    mant = mant.append(sheet2)
    
mnt_asian = mant[mant["Indicator"] == "Percent Asian"]
mnt_black = mant[mant["Indicator"] == "Percent black"]
mnt_hispanic = mant[mant["Indicator"] == "Percent Hispanic"]
mnt_white = mant[mant["Indicator"] == "Percent white"]
#Poverty rate
mnt_poverty = mant[mant["Indicator"] == "Poverty rate"]
#Household income
mnt_income = mant[mant["Indicator"] == "Median household income (2018$)"]
#Units authorized by new building permits
mnt_permits = mant[mant["Indicator"] == "Units authorized by new residential building permits"]

training = training.append([mnt_asian, mnt_black, mnt_hispanic, 
    mnt_white, mnt_poverty, mnt_income, mnt_permits])

# Queens files
for file in queens_xlsx:
    data = pd.ExcelFile("QN/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    queens = queens.append(sheet2)
    
qn_asian = queens[queens["Indicator"] == "Percent Asian"]
qn_black = queens[queens["Indicator"] == "Percent black"]
qn_hispanic = queens[queens["Indicator"] == "Percent Hispanic"]
qn_white = queens[queens["Indicator"] == "Percent white"]

qn_poverty = queens[queens["Indicator"] == "Poverty rate"]
qn_income = queens[queens["Indicator"] == "Median household income (2018$)"]
qn_permits = queens[queens["Indicator"] == "Units authorized by new residential building permits"]


demographics = demographics.append([qn_asian, qn_black, qn_hispanic, qn_white, qn_poverty, qn_income, qn_permits])

# Staten Island files
for file in si_xlsx:
    data = pd.ExcelFile("SI/%s" % file)
    sheet2 = pd.read_excel(data, 1) #extracting only sheet with data
    statisl = statisl.append(sheet2)
    
si_asian = statisl[statisl["Indicator"] == "Percent Asian"]
si_black = queens[statisl["Indicator"] == "Percent black"]
si_hispanic = statisl[statisl["Indicator"] == "Percent Hispanic"]
si_white = statisl[statisl["Indicator"] == "Percent white"]

si_poverty = statisl[statisl["Indicator"] == "Poverty rate"]
si_income = statisl[statisl["Indicator"] == "Median household income (2018$)"]
si_permits = statisl[statisl["Indicator"] == "Units authorized by new residential building permits"]

demographics = demographics.append([si_asian, si_black, si_hispanic, si_white, si_poverty, 
    si_income, si_permits])


cols = [1,2,3,4,6,7, 8,10,11,12,13] #columns irrelevant to analysis
demographics = demographics.drop(demographics.columns[cols],axis=1) #removing irrelevant column
training = training.drop(training.columns[cols], axis = 1)
#removing symbols
demographics[2000] = demographics[2000].map(lambda x: x.lstrip('$').rstrip('%'))
demographics[2018] = demographics[2018].map(lambda x: x.lstrip('$').rstrip('%'))
training[2000] = training[2000].map(lambda x: x.lstrip('$').rstrip('%'))
training[2018] = training[2018].map(lambda x: x.lstrip('$').rstrip('%'))
demographics = demographics.replace(',','', regex=True)
training = training.replace(',','', regex=True)
#converting data frames to floats
demographics[2000] = demographics[2000].astype(float)
demographics[2018] = demographics[2018].astype(float)
training[2000] = training[2000].astype(float)
training[2018] = training[2018].astype(float)


#Bernoulli Classifier
#from sklearn.naive_bayes import BernoulliNB
#model = BernoulliNB()
#model.fit(matrix, target array) 
#model.fit(training, all_boroughs) 
from sklearn.svm import SVC
svclassifier = SVC(kernel='poly', degree=7)
svclassifier.fit(training, demographics)
#from sklearn import svm 
#SVM = svm.LinearSVC()
#SVM.fit(training, demographics)



#model.predict(training) for datapoint predictions 
prediction_gent = model.predict_proba(training) 
gentrified = []    # create an array to store the probability
for i in prediction_gent:
   gentrified.append(i[0])


