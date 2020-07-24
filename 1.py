#Created on Mon Jun  8  2020
#@author: pc
# 1 firstly import os to change directory and Pandas
import os 
import pandas as pd
os.chdir('D:\Repo\Learn-Pandas-with-PaareshC')
# 2 now let us create a dataframe (df)
df=pd.read_csv('mpg.csv')
# 3 Let us study the df first
# 3.1 Shape of df
print(df.shape)
# 3.2 to print out the columns
print(df.columns)
# 3.3 information about df like columns their entriens and their data types
print(df.info())
# 3.4 Numerical analysis like mean , median and differnet percentiles
print(df.describe())
# Now suppose you want a specific column or columns , maybe a row or rows , we will subset what we are interested in '''
# 4 Techniques of subsetting
# 4.1 Suppose i want to subset name column and print it 
name=df['name']
print(name)
# 4.2 now i want names along with horsepower
my_demand=['horsepower','name']
name_with_hp=df[my_demand]
print(name_with_hp)
# 4.3 now suppose i want 4.2 but only cars whose horsepower > 117
hp_greater_than_117=name_with_hp[df['horsepower']>117]
print(hp_greater_than_117)
