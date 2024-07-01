# importing python libraies pandas
import pandas as pd

# pandas is one the library which is used for the purpose of data cleaning and manipulation.
# which is based on dataframe (row,column) and series (1 single column).
# Also used for the purpose of exploring the data

df = pd.read_csv('train.csv')
print(df)

# Understanding the data
type(df)

# To print only first 5 row
df.head()

# to print only last 5 row
df.tail()

# we can pass parameter also

# To know more about our dataset.
df.info()

# To access any column in data through pandas
df['Name']

# To know about total row and column
df.shape

# To find total null value in data set
df.isnull().sum()

df.describe() # this will describe in detail of dataset

# To drop any column or row from dataset
df.drop('Name',axis=1, inplace= True)

# for row
df.drop('Name',axis=0,inplace=True)

# To access any row in data
df.iloc[2]

