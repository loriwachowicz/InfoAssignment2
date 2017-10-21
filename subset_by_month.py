import pandas as pd
import numpy as N
import datetime as dt

infile = pd.read_csv("G://informatics//hourly_obs_cleaned_1980_2009.csv")

dts= pd.to_datetime(infile['Date'], format = '%Y%m%d')
infile.index = dts

df_jan = infile.iloc[(infile.index.month == 1)]
df_feb = infile.iloc[(infile.index.month == 2)]
df_dec = infile.iloc[(infile.index.month ==12)]

#df_combined = df_jan.join(df_feb, how='outer')
#df_combined = df_combined.join(df_dec, how='outer')
df_list = [df_jan,df_feb,df_dec]
df_combined = pd.concat(df_list)

df_final = df_combined.sort_values(['Date','Hour'],ascending=True)

df_final.to_csv("G://informatics//hourly_obs_djf.csv")

