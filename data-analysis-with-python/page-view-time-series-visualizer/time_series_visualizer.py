import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df.date = pd.to_datetime(df.date)
#df.set_index('date',inplace=True)
# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &
   (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize = (21,7))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig = sns.lineplot(data=df, x='date', y='value', color = 'red').figure
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df['date'].dt.year
    df_bar['Month'] = df['date'].dt.month
    df_barg = df_bar.groupby(['Year', 'Month']).mean().unstack()
    mon = ['January', 'February', 'March', 'April' , 'May' , 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig = df_barg.plot(kind = 'bar', figsize=(15, 15)).figure
    plt.xlabel("Years", fontsize = 20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylabel("Average Page Views", fontsize = 20)
    plt.legend(fontsize = 10, labels = mon, prop={"size":20})
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=mon, ordered=True)
    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(figsize=(12, 7), ncols=2, sharex=False)
    sns.despine(left=True)

    ax2 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
