import pandas as pd
#import datetime as dt
#import math
#import numpy as N

df = pd.read_csv("G://informatics//hourly_obs_unclean_1980_2009.csv")

df['Date'] = df['Date'].map(lambda x: x.strip(","))
df['Hour'] = df['Hour'].map(lambda x: x.strip(","))
df['Wind Direction'] = df['Wind Direction'].map(lambda x: x.strip(","))
df['Wind Speed'] = df['Wind Speed'].map(lambda x: x.strip(","))
df['TEMP'] = df['TEMP'].map(lambda x: x.strip(","))
df['DEWPT'] = df['DEWPT'].map(lambda x: x.strip(","))
df['cloud height'] = df['cloud height'].map(lambda x: x.strip(","))
df['total coverage code'] = df['total coverage code'].map(lambda x: x.strip(","))
df['total lowest cloud cover code'] = df['total lowest cloud cover code'].map(lambda x: x.strip(","))
df['low cloud type'] = df['low cloud type'].map(lambda x: x.strip(","))
df['mid cloud type'] = df['mid cloud type'].map(lambda x: x.strip(","))
df['SLP'] = df['SLP'].map(lambda x: x.strip(","))
df['liq precip amt #1'] = df['liq precip amt #1'].map(lambda x: x.strip(","))
df['snowdepth'] = df['snowdepth'].map(lambda x: x.strip(","))
df['water equivalent snowdepth'] = df['water equivalent snowdepth'].map(lambda x: x.strip(","))

df['ObsType'] =  df['ObsType'].map(lambda x: x.strip(","))

df.to_csv("G://informatics//hourly_obs_cleaned_1980_2009.csv")

