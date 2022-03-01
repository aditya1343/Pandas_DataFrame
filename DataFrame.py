import pandas as pd
import numpy as np

#Creating a DataFrame

df  = pd.DataFrame(
{

"S.No" : np.arange(7) ,  #1st Column

"MID" : [ 0 , 0, 0 , 11 , 1 , 8 , 4 ] , #2nd Col

"ASG" : [ 0 , 0 , 5 , 5 , 5 , 5 , 5 ] ,   #3rd Column

"OS" : [ "MID" , "AB" , "AB" , 12 , 10.5 , 15 , 11.5 ] , #4th Column

" ASG " : [ 0 , 5 , 5 , 5 , 5 , 5 , 5 ]  #5th Column

}
)

print(df) #Printing DataFrame

#Task 1 
#Each Column in a DataFrame is a Series

Column_Series_1 = df["S.No"]
Column_Series_2 = df["MID"]
Column_Series_3 = df["ASG"]
Column_Series_4 = df["OS"]
Column_Series_5 = df[" ASG "]

print(Column_Series_1)
print(Column_Series_2)
print(Column_Series_3)
print(Column_Series_4)
print(Column_Series_5)

#Task 2
#Create Dictionary for Each Column and make a Series

Col_dict_1 = { "S.No" : [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ]}
print(pd.Series(Col_dict_1))

Col_dict_2 = { "MID" : [0 , 0, 0, 11 , 1 , 8 , 4 ]}
print(pd.Series(Col_dict_2))

Col_dict_3 = { "ASG" : [ 0 , 0 , 5 , 5 , 5 , 5 , 5 ] }
print(pd.Series(Col_dict_3))

Col_dict_4 = { "OS" : [ "MID" , "AB" , "AB" , 12 , 10.5 , 15 , 11.5 ] }
print(pd.Series(Col_dict_4))

Col_dict_5 = { " ASG " : [  0 , 5 , 5 , 5 , 5 , 5 , 5 ] }
print(pd.Series(Col_dict_5))

#Task 3
# Customizing the index to Roll Numbers

df.index = [ "0" , "20EG107101" , "20EG107102" , "20EG107103" , "20EG107104" , "20EG107105" , "20Eg107106"] 
print(df)

#Task 4
#Check If there is any missing data

print(pd.isnull(df))

#Task 5
#Check the index has any duplicate values

df.index = [ "0" , "20EG107101" , "20EG107102" , "20EG107103" , "20EG107104" , "20EG107105" , "20Eg107106"] 
print(df.duplicated())

#Task 6
#Select the values of assignment greater than 2

asg_df = df[df["ASG"] > 2]
print(asg_df)

#Task 7
#Select the values of mid greater than 4

mid_df = df[df["MID"] > 4]
print(mid_df)
