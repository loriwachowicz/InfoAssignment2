# InfoAssignment3

Purpose of project: To visualize climatological variables for a location (Philadelphia, PA) using available hourly observations from Philadelphia Int’l Airport (KPHL). 
These climatological variables (temperature, wind, and precipitation) are assessed for the winter months (DJF) from 1980 - 2009.
In particular, the following quesitions are asked:
  1. how does mean daily temperature vary by month?
  2. is there a relationship between wind direction and wind speed?
  3. which month receives the most precipitation?

Description of the data:
	Original raw data is not included with submission, but includes hourly and some sub-hourly observations from 1972 through 2015 for several different types of observations. I had already obtained somewhat-tidy data (already subset for 30-year period and not including sub-hourly observations) for the 1980-2009 period, but needed to be stripped of commas (using python script: cleanup.py) and missing values (done in Excel, as it was a smaller file). Therefore the original somewhat-tidy dataset read in by cleanup.py (hourly_obs_unclean_1980_2009.csv) is not included but the completely-tidy dataset (hourly_obs_cleaned_1980_2009_v2.csv) is the data to be used in the analysis. It is important to note that this dataset is not consistent through time, and occasionally there are missing hourly observations that are not accounted for, so any time series analysis may be incomplete.
Also included is a csv containing only hourly observations for the winter months (hourly_obs_djf_v2.csv), though this particular file ended up not being used. The script that was developed to subset these particular months is subset_by_month.py, and can easily be adjusted to subset other months to make another file if the user wishes.

Analysis of Data:
Jupyter Notebook for Python 2.7 (the version of Python on my work computer) is used for plotting and visualizing mean daily temperature, the relationship between wind speed and direction, and monthly average total precipitation using the pandas library, as well as the ‘ggplot’ environment in matplotlib. The computational notebook is found in the InformaticsProject3.ipynb file. In addition, a hard copy of the scripts used to make the plots is located in plotting_script.py.

Additional information:
Data file path will need be changed in the Jupyter Notebook.
Requires pandas, matplotlib, and datetime libraries
