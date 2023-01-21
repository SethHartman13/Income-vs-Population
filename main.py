import glob
import pandas as pd
import os
import numpy as np
from functools import partial
import matplotlib
import matplotlib.pyplot as plt


# Headers
header_income = ['State','County', '2019 Dollars', '2020 Dollars', '2021 Dollars', 'Rank in State ($)', '2020 % change', '2021 % change', 'Rank in State (%)']
header_pop = ['State', 'County', '2020 Population', '2021 Population']

# Allows keyword arguments to be used within the future map function
mapfunc1 = partial(pd.read_csv, header=None, names=header_income)
mapfunc2 = partial(pd.read_csv, header=None, names=header_pop, on_bad_lines='skip')

# Constructs the relative file locations of the .csv's
joined_files_income = os.path.join("./State-Income-CSVs/", "*.csv")
joined_list_income = glob.glob(joined_files_income, )

joined_files_pop = os.path.join("./State-Pop-CSVs/", "*.csv")
joined_list_pop = glob.glob(joined_files_pop, )

# This creates the dataframes to hold the two different datasets (population and income)
df_income = pd.concat(map(mapfunc1, joined_list_income), ignore_index=True)
df_pop = pd.concat(map(mapfunc2, joined_list_pop), ignore_index=True)

# Replaces all NA values with the number 0
df_income = df_income.replace(np.nan, 0)
df_income = df_income.replace("(NA)", 0)
df_income = df_income.replace("--", 0)

df_pop = df_pop.replace(np.nan, 0)
df_pop = df_pop.replace("(NA)", 0)
df_pop = df_pop.replace("--", 0)

# Changes str to ints in the proper columns
for column in header_income:
    if column == "State" or column == "County":
        pass
    else:
        df_income = df_income.astype({column:"float"})
try:
    for column in header_pop:
        if column == "State" or column == "County":
            pass
        else:
            df_pop = df_pop.astype({column:"float"})
except ValueError:
    pass

# Merges the two data sets to be a common singular dataset
commondf = df_income.merge(df_pop, on=['State','County'])

# Creates the scatter plot
ts = commondf.plot.scatter(x = '2020 Population', y = '2020 Dollars', s = 500, marker=".")
ts.plot(markersize=10)


ts2 = commondf.plot.scatter(x = '2021 Population', y = '2021 Dollars', s = 500, marker=".")
ts2.plot(markersize=10)
plt.show()

print(df_income.groupby(['State'])['2020 Dollars'].sum())





# My questions:
# Is there a correlation between population of a county to its income, if so, is it positive or negative?
# No, there is not. We see that lower populated counties have a variety of incomes, it seems to be that population does not affect income.

# Is there a significant change between 2020 and 2021?
# No, there is not a significant change between 2020 and 2021, we see values change slightly, but not significantly. If we want to see some change, we need to have a greater
# time difference.