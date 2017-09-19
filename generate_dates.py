import numpy as np
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

#data loaction
file_name='Calendar2.xlsx'
sheet_name='Working file'
file_path='C:\\Users\\u164345\\OneDrive for Business\\IAG Data\\'

#reading data from excel
def reading(file, sheet, path):
    table=pd.read_excel(path+file,
                        sheetname=sheet,
                        parse_cols='F,M,N,O')
    return table

table=reading(file_name,sheet_name,file_path)
table.columns=('Name','Frequency','First','Last') #renaming columns
Data=pd.DataFrame({'names':[],'dates':[]}) #creating output data structure
for row in table.itertuples(): #iterating row by row and applying logic
	name=row.Name
	end=row.First
	a=[]
	if isinstance(row.First,datetime.date) and isinstance(row.Last,datetime.date): #checking if value is date, if not, this row will be ignored
		while end<=row.Last: #creating new rows per date according to logic
			a.append(end)
			if end==row.Last:
				break
			elif row.Frequency=='once':
				break
			elif row.Frequency=='twice':
				a.append(row.Last)
				break
			elif row.Frequency=='year':
				end+=relativedelta(years=+1)
			elif row.Frequency=='mth':
				end+=relativedelta(months=+1)
			elif row.Frequency=='qtr':
				end+=relativedelta(months=+3)
			elif row.Frequency=='seasonal':
				end+=relativedelta(months=+6)
			else:
				break
	
	length=len(a)
	names=[name]*length
	df=pd.DataFrame({'names':names,'dates':a})
	Data=pd.concat([Data,df])
Result=Data.reset_index(drop=True)

Result.to_csv(file_path+'Dates_generated2.csv',
                  index=False,sep='|') #saving output into file
#print(Result)