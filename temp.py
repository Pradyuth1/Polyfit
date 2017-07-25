import pandas as pd
from numpy import *
import numpy as np
import datetime as DT
import matplotlib.pyplot as plt
from scipy.interpolate import *

#reading the file
df=pd.read_csv('Test 1.csv')

#describing the file
A=df.describe()

#print(A)

dfx=pd.DataFrame(df,columns=['Time_Received','Point_Name','Value'])

#print(dfx)

#deleting rows which has unnecessary information
df1=dfx.drop(dfx[dfx.Point_Name!='Temperature'].index, inplace=False )
#df2=pd.DataFrame(df1)
#print(df1)

df3=dfx.drop(dfx[dfx.Point_Name!='AverageTemp'].index, inplace=False)
df4=dfx.drop(dfx[dfx.Point_Name!='EffectiveSetpoint'].index, inplace=False)
df5=dfx.drop(dfx[dfx.Point_Name!='OperatingState'].index, inplace=False)

#separating the date from time in the Time_Received column 
df6=df1['Time_Received']
#print(df6)

#slicing out the hours from the datetime format
df7=df1.Time_Received.str.slice(-5,-3).astype(int)
#print(df7)

df7.dtypes #to show it is an int type

#converting datetime column into an "int" datetime format
df8=pd.to_datetime(df1.Time_Received)
#print(df8)
df8.dtypes #to show it is in int types

df9=df3.Time_Received.str.slice(-5,-3).astype(int)
df10=df4.Time_Received.str.slice(-5,-3).astype(int)
df11=df5.Time_Received.str.slice(-5,-3).astype(int)

df12=pd.to_datetime(df3.Time_Received)
df13=pd.to_datetime(df4.Time_Received)
df14=pd.to_datetime(df5.Time_Received)

#print(df14.dtypes)
#print(df8.head(6))
DF=pd.concat([dfx,df8])
#print(df8)

#concatening the dataframes df1 and df8
New_Df=pd.concat([df1,df8],axis=1)
#print(New_Df)

New_Df2=pd.concat([df3,df12],axis=1)
New_Df3=pd.concat([df4,df13],axis=1)
New_Df4=pd.concat([df5,df14],axis=1)

New_Df5=New_Df2.drop('Time_Received',axis=1)
New_Df6=pd.concat([New_Df5,df9],axis=1)
#print(New_Df6)
#print(New_Df3)

#Fitting the data into the curve

#def abcd(x,a,b,c):
#    return 1*np.exp(-2*New_Df)+1

#xdata=New_df2
#y=abcd(xdata,1,2,3)

#X,Y=curve_fit(abcd,New_Df2['Value'],New_Df2['Point_Name'])

#A=polyfit(New_Df2[:1],New_Df2[:2],1)

B=pd.to_numeric(New_Df6['Value'],errors='coerce')

C=pd.to_numeric(New_Df6['Time_Received'])

Q=polyfit(C,B,2)

print(Q)

plt.plot([C],[B],'bo')
plt.xlabel('Days')
plt.ylabel('Value')

plt.show























