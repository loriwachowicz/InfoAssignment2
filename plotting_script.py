import matplotlib 
matplotlib.style.use('ggplot')

import pandas as pd
import datetime as dt
import numpy as N

infile = pd.read_csv("G:\\informatics\\hourly_obs_cleaned_1980_2009_v2.csv", na_values= '')
dts= pd.to_datetime(infile['Date'], format = '%Y%m%d')
infile.index = dts

# subset df into dfs by months
df_jan = infile.iloc[(infile.index.month == 1)]
df_feb = infile.iloc[(infile.index.month == 2)]
df_dec = infile.iloc[(infile.index.month ==12)]

# precip data
prec_dec = N.array((df_dec['liq precip amt #1'].sum())/30)
prec_jan = N.array((df_jan['liq precip amt #1'].sum())/30)
prec_feb = N.array((df_feb['liq precip amt #1'].sum())/30)
# plots bar graph of monthly totals
prec = pd.DataFrame([prec_dec,prec_jan,prec_feb],columns= ['Total Avg Precip'])
prec.plot.bar(legend=False, title='Total Average Monthly Precip \n Liquid Equivalent (mm)')

# temp data
temp_dec = df_dec['TEMP'].groupby(df_dec['Date']).mean()
temp_jan = df_jan['TEMP'].groupby(df_jan['Date']).mean()
temp_feb = df_feb['TEMP'].groupby(df_feb['Date']).mean()
#plots distribution of all hourly temperature measurements over 30 year period
temp_dec.plot.hist(alpha=0.5,legend=True,label='Dec')
temp_jan.plot.hist(alpha=0.5,legend=True,label='Jan')
temp_feb.plot.hist(alpha=0.5,legend=True,label='Feb')
#temp_dec.plot(kind='hist',alpha=0.5,legend=True,label='Dec')
#temp_jan.plot(kind='hist',alpha=0.5,legend=True,label='Jan')
#temp_feb.plot(kind='hist',alpha=0.5,legend=True,label='Feb')

# scatter plot of relationship between wind speed and direction
df_dec.plot.scatter(x='Wind Direction',y='Wind Speed',legend=True,label='Dec')
df_jan.plot.scatter(x='Wind Direction',y='Wind Speed',legend=True,label='Jan')
df_feb.plot.scatter(x='Wind Direction',y='Wind Speed',legend=True,label='Feb')
# hexbin to better visualize relationship between wind speed and direction
df_dec.plot.hexbin(x='Wind Direction',y='Wind Speed',title='Dec')
df_jan.plot.hexbin(x='Wind Direction',y='Wind Speed',title='Jan')
df_feb.plot.hexbin(x='Wind Direction',y='Wind Speed',title='Feb')

