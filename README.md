# Analyzing-Unemployment-Trends-California
OOP Final Project - Spring 2026

# Analyzing Unemployment Trends in California

An ETL (Extract, Transform, Load) project that compares how California's unemployment rate moved across age groups during two major economic shocks: the **2008 Financial Crisis** and the **COVID-19 pandemic**.

## Overview

The script `final.py` loads California unemployment data broken down by age group, isolates the time windows for each crisis, finds the peak unemployment rate for each age group, labels each crisis by severity, and produces two charts for comparison.

## Dataset

- **Source:** [Unemployment Rate by Age Groups (Data.gov)](https://catalog.data.gov/dataset/unemployment-rate-by-age-groups)
- **Expected file:** `unemployment_data.csv` (placed in the same folder as `final.py`)
- **Required columns:** `Date`, `Age 16-19`, `Age 20-24`, `Age 25-34`, `Age 35-44`, `Age 45-54`, `Age 55-64`, `Age 65+`

Rates are expected as decimals (e.g., `0.10` = 10%).

## How It Works

### 1. Extract
Reads `unemployment_data.csv` with pandas and converts the `Date` column to datetime.

### 2. Transform
- Filters the data into two crisis windows:
  - **2008 Financial Crisis:** 2008-09-16 to 2009-06-01
  - **COVID-19:** 2020-03-13 to 2023-05-05
- Finds the maximum unemployment rate for each age group in each window.
- Assigns a severity label to each crisis based on its highest rate:

| Peak rate | Label |
|-----------|-------|
| 20% or more | Severe (20%+) |
| 10% to under 20% | Moderate (10-20%) |
| Under 10% | Mild (<10%) |

### 3. Load
Generates and saves two charts (each also displayed on screen):

1. **`UnemploymentChart.jpg`**: line chart of unemployment over time for all age groups, with the 2008 crisis in purple and COVID-19 in blue.
2. **`HighestUnemploymentChart.jpg`**: grouped bar chart of peak unemployment rate by age group for each crisis.

## Requirements

- Python 3.8+
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)

Install dependencies:

```bash
pip install pandas matplotlib
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/smandava017/Analyzing-Unemployment-Trends-California.git
   cd Analyzing-Unemployment-Trends-California
   ```
2. Download the dataset from the link above and save it as `unemployment_data.csv` in the project folder.
3. Run the script:
   ```bash
   python final.py
   ```
4. Close the first chart window to display the second one.

## Output

Console output:

```
Extract:
Data Loaded!
Transform:
2008 Crisis severity: <label>
COVID Crisis severity: <label>
Load:
Charts saved!
```

Files created in the project folder:
- `UnemploymentChart.jpg`
- `HighestUnemploymentChart.jpg`

## Project Structure

```
.
├── final.py                     # ETL pipeline and visualizations
├── unemployment_data.csv        # Input dataset (download separately)
├── UnemploymentChart.jpg        # Generated line chart
└── HighestUnemploymentChart.jpg # Generated bar chart
```

## Notes and Possible Improvements

- Both crises are drawn in single colors in the line chart, so individual age groups are not distinguishable there; the bar chart shows the per-group comparison.
- Crisis date ranges and severity thresholds are hard-coded and can be adjusted at the top of the Transform section.
- The two crisis windows have different lengths, so the line chart plots them on a shared calendar axis rather than aligned by months since the start.

## Author

[smandava017](https://github.com/smandava017)
