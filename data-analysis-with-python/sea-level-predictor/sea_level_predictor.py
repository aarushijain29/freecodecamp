import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    years = list(range(1880, 2051, 1))
    line = [intercept + slope * j for j in years]
    plt.plot(years, line, linewidth=2, color="r")

    # Create second line of best fit
    mod_df = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x=mod_df["Year"], y=mod_df["CSIRO Adjusted Sea Level"])
    years2 = list(range(2000, 2051, 1))
    line2 = [intercept2 + slope2 * j for j in years2]
    plt.plot(years2, line2, linewidth=3, color="k")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()