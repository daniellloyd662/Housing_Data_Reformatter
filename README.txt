The python file will loop through all csv files in the current directory and create a copy for each file with the contents reformatted
A folder will be created in the current directory and all reformatted python files will be moved there under the same name as the original

Reformatting consists of:
	Removing all columns that are empty or do not contain one of the specified keywords in the python file
	Moving one of the columns (typically unit type) to left of the table and sorting the dataset in ascending order
	Filtering out all rows except the lowest rent for each unit type

Before running the script make the following changes:
	firstcolumn: 
		type in the name of the column header for all entries will be sorted (typically unit type)
	price: 
		type in the column header for which the minimum price for each floor will be checked (typically rent or price)
	keywords:
		Include keywords indicating which columns to keep in the reformatted data set.
		Any column header which contains a keyword will be kept if it is not empty
		Formatting:
			add and remove keywords in quotes, seperated by commas
			Ex: ['unit', 'rent', ..., 'floor']
			