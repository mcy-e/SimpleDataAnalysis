import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


dt= pd.read_csv("BackEnd/Tables/csv/data_set.csv")

#?  1.Line chart – Monthly trends for all cities 

dt.plot.line()
plt.grid(True,alpha=0.3)
plt.gca().set_axisbelow(True)
plt.title("Monthly trends for all cities")
plt.ylabel("Temperature")
plt.xlabel("Months")
plt.savefig("BackEnd/Graphs/Monthly_trends_for_all_cities.png")
plt.show()

   
#? 2.Box plot – Compare distributions 

'''
    dt.plot.box()
    plt.grid(True,alpha=0.3)
    plt.gca().set_axisbelow(True)
    plt.title("Distributions For the all cities")
    plt.ylabel("Temperature")
    plt.xlabel("Cities")
    plt.savefig("BackEnd/Graphs/Distributions_For_the_three_cities.png")
    plt.show()

'''

#? 3. Histogram – Frequency distribution for one city

'''
    dt["London"].plot.hist(color='blue',edgecolor='black')
    plt.grid(True,alpha=0.3)
    plt.gca().set_axisbelow(True)
    plt.title("Frequency distribution for one London ")
    plt.ylabel("Frequency")
    plt.xlabel("Values range")
    plt.savefig("BackEnd/Graphs/Frequency_distribution_for_one_London.png")
    plt.show()

'''

#? Violin plot – Density and distribution combined

'''
    sns.violinplot(data=dt)
    plt.grid(True,alpha=0.3)
    plt.gca().set_axisbelow(True)
    plt.title("Density and distribution for all cities")
    plt.ylabel("Temperature")
    plt.xlabel("Cities")
    plt.savefig("BackEnd/Graphs/Density_and_distribution_for_all_cities.png")
    plt.show()

'''

# ax = df.plot()
# ax.get_figure().savefig('my_plot.png')

# plt.figure(figsize=(10, 6))

# df.plot()

# plt.savefig('high_quality_graph.jpg', dpi=300)