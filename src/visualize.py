import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

def revenue(df, feat, param):
    revenues_df = df.loc[df[feat] == param].copy()
    revenues_df['date'] = pd.to_datetime(revenues_df['date'])
    revenues_df = revenues_df.groupby('date')['revenues'].sum().reset_index()
    revenues_df = revenues_df.set_index('date')
    return revenues_df

def color():
    colors = ["blue", "black", "brown", "red", "yellow", "green", "orange"]
    random.shuffle(colors)
    return colors[0]


def bar_department(total_revenues, total_sales, avg_price):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    width = 0.25
    x = np.arange(len(total_revenues["dept_id"]))

    # Plot the first graph (Total Revenues)
    axes[0].bar(x, total_revenues["revenues"], width, color='b', label='Total Revenues')
    axes[0].set_title("Total Revenues across Departments", fontsize=15)
    axes[0].set_ylabel("Revenues", fontsize=13)
    axes[0].set_xlabel("Department", fontsize=13)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(total_revenues["dept_id"], rotation=90)
    axes[0].legend()

    # Plot the second graph (Total Sales)
    axes[1].bar(x, total_sales["sales"], width, color='g', label='Total Sales')
    axes[1].set_title("Total Sales across Departments", fontsize=15)
    axes[1].set_ylabel("Sales", fontsize=13)
    axes[1].set_xlabel("Department", fontsize=13)
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(total_sales["dept_id"], rotation=90)
    axes[1].legend()

    # Plot the third graph (Average Price)
    axes[2].bar(x, avg_price["sell_price"], width, color='r', label='Average Price')
    axes[2].set_title("Average Price across Departments", fontsize=15)
    axes[2].set_ylabel("Avg Price", fontsize=13)
    axes[2].set_xlabel("Department", fontsize=13)
    axes[2].set_xticks(x)
    axes[2].set_xticklabels(avg_price["dept_id"], rotation=90)
    axes[2].legend()

    # Adjust the layout to avoid overlapping
    plt.tight_layout()

    # Show the subplots
    plt.show()