import pandas
import numpy as np
import os

#==========================================User Editable variables: Make changes here to affect script performance===================================

#Firstcolumn specifies whatever column will be at index 0
firstcolumn='unit type name'

#price specifies which column will be checked for lowest possible rent
price = "max rent"

#Specifies the name of the folder where reformatted csv files will be stored
foldername = 'Reformatted'

#Columns containing these keywords will be copied into the reformatted csv file if they are not empty, all other columns will be deleted
#Leave, 'firstcolumn' and price variables, all other strings can be modified, added, or removed

keywords = [price, firstcolumn,'unit', 'rent', 'price', 'sq', 'floor']
#====================================================================================================================================================



#=========================================
#Reformat passed in file
def Reformat(filename):
    #Open data with pandas library
    df = pandas.read_csv(filename)

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
    #keywords = ['unit', 'rent', 'price' 'sq', 'floor']

    #Filter all column headers containing a keyword string
    def filterkeywords(words):
        returnedcolumns = set([])
        #print(df.columns)
        for word in keywords:
            collist = list(df.filter(like= word).columns)
            returnedcolumns.update(collist)
        return returnedcolumns
    
    columns = filterkeywords(keywords)
    #print(columns)
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


    df = df.filter(items = minimumids, axis=0)
    #Save to new csv file
    df.to_csv("./"+foldername+"/"+filename, sep=',', index=False)

def createPath(folder):
    path = "./" + foldername
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
    # Create a new directory because it does not exist 
        os.makedirs(path)

createPath(foldername)

#Loop through each csv file in the current directory, reformat and copy to the
csvfiles=[]
for file in os.listdir("./"):
    if file.endswith(".csv"):
        csvfiles.append(file)
        Reformat(file)