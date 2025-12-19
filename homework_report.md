# City Temperature Analysis - Homework Report

---

## ANSWER SECTION

### Part 1: Data Import & Basic Summaries

#### 1. Import the data into EViews, SPSS, R, or Python

The data was successfully imported into Python using the Pandas library. The dataset was created as a DataFrame with three cities (London, Paris, Rome) and 12 months of temperature data.

#### 2. Calculate for each city:

##### Mean, Median, Mode

| City | Mean | Median | Mode |
|------|------|--------|------|
| **London** | 12.417°C | 12.0°C | 6, 9, 20 |
| **Paris** | 13.0°C | 13.0°C | 9, 22 |
| **Rome** | 17.917°C | 17.5°C | 10, 28 |

##### Range, Variance, Standard Deviation

| City | Range | Variance | Standard Deviation |
|------|-------|----------|-------------------|
| **London** | 15°C | 28.076 | 5.299 |
| **Paris** | 18°C | 38.333 | 6.191 |
| **Rome** | 20°C | 46.910 | 6.849 |

##### Quartiles (Q1, Q3) and IQR

| City | Q1 | Q3 | IQR |
|------|----|----|-----|
| **London** | 8.25°C | 17.25°C | 9.0 |
| **Paris** | 8.25°C | 18.25°C | 10.0 |
| **Rome** | 12.25°C | 24.25°C | 12.0 |

#### 3. Compare:

##### Which city has the highest average temperature?

**Rome** has the highest average temperature with **17.917°C**.

##### Which has the most consistent temperatures (lowest variability)?

**London** has the most consistent temperatures with the lowest standard deviation of **5.299**.

---

### Part 2: Multiple Graphical Representations

Four different visualizations were created to analyze the temperature data:

#### 1. Line Chart – Monthly trends for all cities

![Line Chart - Monthly Trends](d:\Simple-Data-Analysis-Project\BackEnd\Graphs\line_chart.png)

This line chart displays the monthly temperature trends for all three cities throughout the year. It clearly shows:
- All cities follow a similar seasonal pattern with peak temperatures in July-August
- Rome consistently maintains higher temperatures across all months
- London and Paris have very similar patterns, with Paris slightly warmer

#### 2. Box Plot – Compare distributions

![Box Plot - Distribution Comparison](d:\Simple-Data-Analysis-Project\BackEnd\Graphs\box_plot.png)

The box plot compares the temperature distributions across the three cities, showing:
- Rome has the highest median temperature
- Rome shows greater spread in the data (larger IQR)
- London has the most compact distribution, indicating more consistent temperatures

#### 3. Histogram – Frequency distribution for one city

![Histogram - Paris Frequency Distribution](d:\Simple-Data-Analysis-Project\BackEnd\Graphs\histogram_paris.png)

This histogram shows the frequency distribution of temperatures for Paris:
- Temperatures are distributed across different ranges
- Shows the concentration of temperature values throughout the year
- Helps identify the most common temperature ranges

#### 4. Violin Plot – Density and distribution combined

![Violin Plot - Density and Distribution](d:\Simple-Data-Analysis-Project\BackEnd\Graphs\violin_plot.png)

The violin plot combines density estimation with distribution visualization:
- Shows the probability density of temperatures at different values
- Rome displays the widest distribution with higher temperature ranges
- Paris shows a relatively symmetric distribution
- London has the most concentrated distribution around the median

---

### Additional Questions

#### Based on the relationship between mean, median, and mode, describe the skewness of each city's temperature distribution.

| City | Mean | Median | Skewness Description |
|------|------|--------|---------------------|
| **London** | 12.417 | 12.0 | **Approximately symmetric** (mean ≈ median) |
| **Paris** | 13.0 | 13.0 | **Approximately symmetric** (mean = median) |
| **Rome** | 17.917 | 17.5 | **Approximately symmetric** (mean ≈ median) |

All three cities show approximately symmetric distributions, as the difference between mean and median is minimal (within tolerance of 0.5°C).

#### Looking at the histograms and density plots, which city's temperatures most closely approximate a normal distribution?

**Paris's temperature distribution most closely approximates a normal distribution.**

Based on the violin plots analysis:
- Paris's density is **symmetric around the median**, with a single central peak and smoothly decreasing tails
- London shows **slight skewness**
- Rome exhibits a **noticeable right skew** with greater variability

---

## TECHNICAL SECTION

### How Pandas Was Used in This Project

This project extensively utilized the **Pandas library** for data manipulation, statistical analysis, and data export. Below is a detailed explanation of how Pandas was applied throughout the analysis.

#### 1. Data Import and DataFrame Creation

The temperature data was structured as a dictionary and converted into a Pandas DataFrame:

```python
import pandas as pd

raw_data = {
    "London": [5,6,9,11,15,18,20,20,17,13,9,6],
    "Paris":  [4,5,9,12,16,19,22,22,18,14,9,6],
    "Rome":   [8,10,13,16,20,25,28,28,24,19,14,10]
}

indexes = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# Create a DataFrame with custom index
data = pd.DataFrame(raw_data, index=indexes)
```

**Key Pandas Features Used:**
- `pd.DataFrame()`: Converts dictionary to structured tabular data
- Custom index assignment for month names
- Multiple columns (cities) created automatically from dictionary keys

#### 2. Statistical Calculations Using Pandas Methods

Pandas provides built-in methods for calculating descriptive statistics:

```python
# Mean calculation
mean = {city: float(data[city].mean().round(3)) for city in data}

# Median calculation
median = {city: float(data[city].median()) for city in data}

# Mode calculation
mode = {city: list(data[city].mode()) for city in data}

# Range calculation
Range = {city: int(data[city].max() - data[city].min()) for city in data}

# Variance calculation (population variance with ddof=0)
Variance = {city: float(data[city].var(ddof=0).round(3)) for city in data}

# Standard deviation calculation (population std with ddof=0)
sd = {city: float(data[city].std(ddof=0).round(3)) for city in data}

# Quartile calculations
q1 = {city: float(data[city].quantile(0.25).round(3)) for city in data}
q3 = {city: float(data[city].quantile(0.75).round(3)) for city in data}
```

**Key Pandas Methods:**
- `.mean()`: Calculate average temperature
- `.median()`: Find middle value
- `.mode()`: Identify most frequent values
- `.max()` and `.min()`: Find extreme values
- `.var()`: Calculate variance
- `.std()`: Calculate standard deviation
- `.quantile()`: Calculate quartiles
- `.round()`: Round numerical results

#### 3. Data Aggregation and Summary Table

All statistics were aggregated into a comprehensive summary table:

```python
stats = {
    "Mean": [mean[city] for city in data],
    "Mode": [mode[city] for city in data],
    "Median": [median[city] for city in data],
    "Range": [Range[city] for city in data],
    "Variance": [Variance[city] for city in data],
    "Std": [sd[city] for city in data],
    "Q1": [q1[city] for city in data],
    "Q3": [q3[city] for city in data],
    "IQR": [iqr[city] for city in data]
}

stats_table = pd.DataFrame(stats, index=data.columns)
```

**Key Features:**
- Creating a new DataFrame from calculated statistics
- Using original column names as the new index

#### 4. Data Analysis and Comparison

Pandas was used to perform comparative analysis:

```python
# Find city with highest average temperature
city_highest_at = stats_table['Mean'].idxmax()

# Find city with most consistent temperatures (lowest standard deviation)
city_most_cons_temp = stats_table['Std'].idxmin()
```

**Key Pandas Methods:**
- `.idxmax()`: Returns index (city name) with maximum value
- `.idxmin()`: Returns index (city name) with minimum value

#### 5. Data Export to Multiple Formats

The results were exported to both JSON and CSV formats:

```python
# Export to JSON
stats_table.to_json("BackEnd/Tables/json/stats_table.json")
data.to_json("BackEnd/Tables/json/data_set.json")

# Export to CSV
stats_table.to_csv("BackEnd/Tables/csv/stats_table.csv")
data.to_csv("BackEnd/Tables/csv/data_set.csv")
```

**Key Pandas Methods:**
- `.to_json()`: Export DataFrame to JSON format
- `.to_csv()`: Export DataFrame to CSV format

#### 6. Reading Data for Visualization

Pandas was used to read the exported CSV files for visualization:

```python
# Read CSV data for plotting
dt = pd.read_csv("BackEnd/Tables/csv/data_set.csv")

# Plot directly from DataFrame
dt.plot.line()  # Line chart
dt.plot.box()   # Box plot
dt["London"].plot.hist()  # Histogram
```

**Key Pandas Features:**
- `pd.read_csv()`: Import CSV data
- `.plot.line()`, `.plot.box()`, `.plot.hist()`: Built-in plotting methods
- Direct integration with Matplotlib for visualization

#### 7. Index Manipulation for Analysis

```python
# Read CSV and set custom index
dt = pd.read_csv("BackEnd/Tables/csv/stats_table.csv")
dt = dt.set_index('Unnamed: 0')

# Access data by index label
mean = dt.loc[city, 'Mean']
median = dt.loc[city, 'Median']
```

**Key Pandas Methods:**
- `.set_index()`: Set a column as the DataFrame index
- `.loc[]`: Label-based data access

### Summary of Pandas Benefits

The Pandas library provided:
1. **Efficient data structure** for tabular temperature data
2. **Built-in statistical functions** eliminating manual calculations
3. **Easy data manipulation** with intuitive syntax
4. **Multiple export formats** for data sharing and visualization
5. **Seamless integration** with visualization libraries (Matplotlib, Seaborn)
6. **Readable and maintainable code** through high-level abstractions

---

**Report Generated:** 2025-12-19  
**Project:** Simple Data Analysis - City Temperature Variations
