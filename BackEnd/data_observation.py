import pandas as pd


dt=pd.read_csv("BackEnd/Tables/csv/stats_table.csv")

dt = dt.set_index('Unnamed: 0')

#* Based on the relationship between mean, median, and mode, describe the skewness of each city's temperature distribution. 

tolerance = 0.1

for city in dt.index:
    mean = dt.loc[city, 'Mean']
    median = dt.loc[city, 'Median']

    if abs(mean - median) < tolerance:
        skew = "approximately symmetric"
    elif mean > median:
        skew = "right-skewed"
    else:
        skew = "left-skewed"

    print(f"The skewness is {skew} for {city}")


# Looking at the histograms and density plots, which i's temperatures most closely approximate a normal distribution? 

'''

    Based on the violin plots, Paris’s temperature distribution most closely approximates a normal distribution. 
    Its density is symmetric around the median, with a single central peak and smoothly decreasing tails. 
    London shows slight skewness
    , while Rome exhibits a noticeable right skew with greater variability

'''