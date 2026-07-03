import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data and set index
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data: remove top and bottom 2.5%
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df.index, df["value"], color="red", linewidth=0.8)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    df_grouped.columns = month_names

    fig, ax = plt.subplots(figsize=(12, 7))
    df_grouped.plot(kind="bar", ax=ax)

    ax.set_title("")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=month_names)

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

    sns.boxplot(data=df_box, x="year", y="value", ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
