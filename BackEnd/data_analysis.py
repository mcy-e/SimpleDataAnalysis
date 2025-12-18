#* import pandas () library
import pandas as pd 

#* get the data set and prepare it for panda

raw_data = {
        
    "London": [5,6,9,11,15,18,20,20,17,13,9,6],
    "Paris":  [4,5,9,12,16,19,22,22,18,14,9,6],
    "Rome":   [8,10,13,16,20,25,28,28,24,19,14,10]
    
}

indexes=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


#* create a data frame
data = pd.DataFrame(raw_data,index=indexes)

#* to check the data
# print(data.to_string())

#? Calculating some Statistics vals

#& Mean
mean={city:float(data[city].mean().round(3)) for city in data}

print(f"mean : {mean}\n")

#& Mode 
mode={city:list(data[city].mode()) for city in data}

print(f"mode : {mode}\n")

#& Median
median= {city:float(data[city].median()) for city in data}

print(f"median : {median}\n")

#& Range 
Range = {city:int(data[city].max()-data[city].min()) for city in data}

print(f"Range : {Range}\n")


#& Variance 
Variance = {city:float(data[city].var(ddof=0).round(3)) for city in data}

print(f"Variance : {Variance}\n")

#& Standard Deviation 
sd= {city:float(data[city].std(ddof=0).round(3)) for city in data}

print(f"Standard Deviation  : {sd}\n")


#& Quartiles  
q1= {city:float(data[city].quantile(0.25).round(3)) for city in data}

print(f"First Quartile: {q1}\n")

q3= {city:float(data[city].quantile(0.75).round(3)) for city in data}

print(f"Third Quartile: {q3}\n")


#& IQR 
iqr={city:q3[city]-q1[city] for city in data}

print(f"IQR: {iqr}\n")

stats={
    "Mean": [mean[city] for city in data],
    "Mode" :[mode[city] for city in data],
    "Median":[median[city] for city in data],
    "Range" : [Range[city]for city in data],
    "Variance":[Variance[city] for city in data],
    "Std": [sd[city] for city in data],
    "Q1": [q1[city] for city in data],
    "Q3": [q3[city] for city in data],
    "IQR": [iqr[city] for city in data]
}

stats_table = pd.DataFrame(stats, index=data.columns)

print(stats_table.to_string())
print("\n")

#* Which city has the highest average temperature?

# We find the max mean

city_highest_at=stats_table['Mean'].idxmax()

print(f"City that has the highest average temperature is : {city_highest_at} \n")


#* Which has the most consistent temperatures?

# We find min std

city_most_cons_temp=stats_table['Std'].idxmin()

print(f"City that has the most consistent temperatures is : {city_most_cons_temp}\n")


#* Save the stats table into a simple file 

import os
os.makedirs("BackEnd/Tables/json", exist_ok=True)
os.makedirs("BackEnd/Tables/csv", exist_ok=True)

stats_table.to_json("BackEnd/Tables/json/stats_table.json")
data.to_json("BackEnd/Tables/json/data_set.json")


stats_table.to_csv("BackEnd/Tables/csv/stats_table.csv")
data.to_csv("BackEnd/Tables/csv/data_set.csv")
