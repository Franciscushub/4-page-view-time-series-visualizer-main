import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,header=0,sep=',')
df.index = pd.to_datetime(df.index)
# Clean data - filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] < df['value'].quantile(0.975))&(df['value'] > df['value'].quantile(0.025))]



def draw_line_plot():
    # Draw line plot - The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
    
    fig, ax = plt.subplots(figsize=(30, 10))
    ax.plot(df,color = 'red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=20)  # Set font size to 20
    plt.xlabel('Date', fontsize=15)  # Set font size to 15
    plt.ylabel('Page Views', fontsize=15) 

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar['month']

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar.columns = pd.to_datetime(df_bar.columns, format='%m').strftime('%B')
    
    # # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 10))
    df_bar.plot(kind='bar', ax = ax, legend=True, fontsize=12)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Average Page Views", fontsize=12)

    # # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(1,2,figsize=(25, 10))
    sns.boxplot(x="year", y="value",data=df_box, ax=ax[0],palette= sns.color_palette())
    ax[0].set_xlabel('Year', fontsize=14) # Set x-axis label
    ax[0].set_ylabel('Page Views', fontsize=14) # Set y-axis label
    ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=16) # Set plot title
    sns.boxplot(x="month", y="value",data=df_box, ax=ax[1],palette= sns.color_palette("husl", 12),order=month_order)
    ax[1].set_xlabel('Month', fontsize=14) # Set x-axis label
    ax[1].set_ylabel('Page Views', fontsize=14) # Set y-axis label
    ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=16) # Set plot title

    plt.subplots_adjust(left=0.07, right=0.97, bottom=0.1, top=0.9, wspace=0.15)






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig