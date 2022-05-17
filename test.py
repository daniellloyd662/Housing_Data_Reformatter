import pandas
import numpy as np


firstcolumn="unit type name"
price = "max rent"

#Open data with pandas library
df = pandas.read_csv('HousingData.csv')

#Sort by unit number
df.sort_values([firstcolumn], axis=0, ascending=[True], inplace=True)

#Move unit type name column to index 0
column_to_move = df.pop("unit type name")
# insert column with insert(location, column_name, column_value)
df.insert(0, firstcolumn, column_to_move)

#Replace empty strings with Nan and remove empty columns
df.replace('', np.nan, inplace=True)
df.dropna(how='all', axis=1,inplace=True)

#Specify which keywords a column must contain to not be deleted
keywords = ['unit', 'rent', 'price' 'sq', 'floor']

#Filter all column headers containing a keyword string
def filterkeywords(words):
    returnedcolumns = []
    for word in keywords:
        returnedcolumns.extend(list(df.filter(like= word).columns))
    return returnedcolumns
columns = filterkeywords(keywords)

#Filter for only columns containing keywords (saved as a list in the columns variable)
df = df[columns]

#================================================Find min rent================================================
uniquefirstcolvalues = list(df.iloc[:, 0].unique())

#Create boolean mask for each unique entry in the first column
minimumids=[]
for uniqueval in uniquefirstcolvalues:
    dfmask = df[firstcolumn]==uniqueval
    dffiltered = df[dfmask]
    if len(dffiltered[[price]])>0:
        minimumids.append(dffiltered[[price]].idxmin()[0])
        # print(dffiltered[[price]].idxmin())
print(minimumids)

df = df.filter(items = minimumids, axis=0)
print(df)
#Save to new csv file
df.to_csv('Testdata.csv', sep=',', index=False)
