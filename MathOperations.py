import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.close("all")


def get_average_value(data):
    return np.average(data)


def get_average_median_value(data):
    return np.median(data)


def get_standard_deviation(data):
    return np.std(data)


def get_expected_value(data):
    return np.mean(data)


def print_plot(dataframe):
    data = dataframe
    df = pd.DataFrame(data)
    columns = list(df.head())
    print(columns)
    df.plot(x=columns[0], y=[columns[1], columns[2]], kind='bar', figsize=(10, 5))
    plt.show()
