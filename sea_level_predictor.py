import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7)

    # Create first line of best fit
    result1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series([i for i in range(df['Year'].min(), 2051)])
    best_fit_1 = [result1.slope * year + result1.intercept for year in years_all]
    plt.plot(years_all, best_fit_1, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    result2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    best_fit_2 = [result2.slope * year + result2.intercept for year in years_recent]
    plt.plot(years_recent, best_fit_2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.title('Rise in Sea Level', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Sea Level (inches)', fontsize=12)
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()