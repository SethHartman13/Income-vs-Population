# Overview

I am trying to learn how to analyze data using datasets found accessable to the general public. Although I already know how to analyze data using Tableau,
I wanted to build my toolkit to include Pandas (Python) Note: Only run main.py.

I am analyzing two data sets, one listing the income of individual counties and one looking at populations.

Income per capita = https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas
Population = https://www.census.gov/data/tables/time-series/demo/popest/2020s-counties-total.html

I wanted to learn how to process data using python's libraries matplotlib and pandas

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/idTrQlUiuRw)

# Data Analysis Results

Is there a correlation between population of a county to its income, if so, is it positive or negative?
No, there is not. We see that lower populated counties have a variety of incomes, it seems to be that population does not affect income.

 Is there a significant change between 2020 and 2021?
 No, there is not a significant change between 2020 and 2021, we see values change slightly, but not significantly. If we want to see some change, we need to have a greater
 time difference.

# Development Environment
I primarily used Pandas and Pandas' built-in way of using Matplotlib to disply graphs.

I used Python, within Python I used the following libraries:
glob
pandas
os
numpy
functools
matplotlib

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Earthly](https://earthly.dev/blog/csv-python/)
* [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min)


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Find more efficient way to split up the csvs and to construct them.
* Find a more efficient way to run the program so that it is not "slow" on older computers (like my laptop).
* I will need to redo the splitting/reformating of the csvs so that it is easier to actually program.