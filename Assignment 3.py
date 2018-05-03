import re
import pandas as pd
import numpy as np
import preprocessing

file = open('wine-data.txt', 'r')
for line in file:
    values = re.split(', |\n|', line)

dataFrame = pd.io.parsers.read_csv('wine-data.txt', header = None, usecols = [0,1,2,3,4,5,6,7,8,9,10,11,12])
dataFrame.columns = ['Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavinoids', 'Nonflavinoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
print('Alcohol max = ', dataFrame['Alcohol'].max(), 'Min = ', dataFrame['Alcohol'].min())
print('Malic Acid max = ', dataFrame['Malic Acid'].max(), 'Min = ', dataFrame['Malic Acid'].min())
print('Ash Max = ', dataFrame['Ash'].max(), 'Min = ', dataFrame['Ash'].min())
print('Alcalinity of ash max = ', dataFrame['Alcalinity of ash'].max(), 'Min = ', dataFrame['Alcalinity of ash'].min())
print('Magnesium max = ', dataFrame['Magnesium'].max(), 'Min = ', dataFrame['Magnesium'].min())
print('Total phenols max = ', dataFrame['Total phenols'].max(), 'Min = ', dataFrame['Total phenols'].min())
print('Flavinoids max = ', dataFrame['Flavinoids'].max(), 'Min = ', dataFrame['Flavinoids'].min())
print('Nonflavinoid phenols max = ', dataFrame['Nonflavinoid phenols'].max(), 'Min = ', dataFrame['Nonflavinoid phenols'].min())
print('Proanthocyanins max = ', dataFrame['Proanthocyanins'].max(), 'Min = ', dataFrame['Proanthocyanins'].min())
print('Color intensity max = ', dataFrame['Color intensity'].max(), 'Min = ', dataFrame['Color intensity'].min())
print('Hue max = ', dataFrame['Hue'].max(), 'Min = ', dataFrame['Hue'].min())
print('OD280/OD315 of diluted wines max = ', dataFrame['OD280/OD315 of diluted wines'].max(), 'Min = ', dataFrame['OD280/OD315 of diluted wines'].min())
print('Proline max = ', dataFrame['Proline'].max(), 'Min = ', dataFrame['Proline'].min())

print('The std deviation of Alcohol is, ', dataFrame.loc['Alcohol'].std())
print('The std deviation of Malic Acid is, ', dataFrame.loc['Malic Acid'].std())
print('The std deviation of Ash is, ', dataFrame.loc['Ash'].std())
print('The std deviation of Alcalinity is, ', dataFrame.loc['Alcalinity'].std())
print('The std deviation of Magnesium is, ', dataFrame.loc['Magnesium'].std())
print('The std deviation of Total phenols is, ', dataFrame.loc['Total phenols'].std())
print('The std deviation of Flavinoids is, ', dataFrame.loc['Flavinoids'].std())
print('The std deviation of Nonflavinoid phenols is, ', dataFrame.loc['Nonflavinoid phenols'].std())
print('The std deviation of Protocyanis is, ', dataFrame.loc['Protocyanis'].std())
print('The std deviation of Color intensity is, ', dataFrame.loc['Color intensity'].std())
print('The std deviation of Hue is, ', dataFrame.loc['Hue'].std())
print('The std deviation of OD280/OD315 is, ', dataFrame.loc['OD280/OD315'].std())
print('The std deviation of Proline is, ', dataFrame.loc['Proline'].std())

dataFrame['Alcohol'] = dataFrame['Alcohol'].apply(lambda x: x *2)
dataFrame['Malic Acid'] = dataFrame['Malic Acid'].apply(lambda x: x *2)
dataFrame['Ash'] = dataFrame['Ash'].apply(lambda x: x *2)
dataFrame['Alcalinity'] = dataFrame['Alcalinity'].apply(lambda x: x *2)
dataFrame['Magnesium'] = dataFrame['Magnesium'].apply(lambda x: x *2)
dataFrame['Total phenols'] = dataFrame['Total phenols'].apply(lambda x: x *2)
dataFrame['Flavinoids'] = dataFrame['Flavinoids'].apply(lambda x: x *2)
dataFrame['Nonflavinoid phenols'] = dataFrame['Nonflavinoid phenols'].apply(lambda x: x *2)
dataFrame['Protocyanis'] = dataFrame['Protocyanis'].apply(lambda x: x *2)
dataFrame['Color intensity'] = dataFrame['Color intensity'].apply(lambda x: x *2)
dataFrame['Hue'] = dataFrame['Hue'].apply(lambda x: x *2)
dataFrame['OD280/OD315'] = dataFrame['OD280/OD315'].apply(lambda x: x *2)
dataFrame['Proline'] = dataFrame['proline'].apply(lambda x: x *2)

print('After performing lambda functions:')
print(dataFrame)
