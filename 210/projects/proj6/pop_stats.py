import json
import statistics as stat
import pandas as pd
from tabulate import tabulate

def read_data(file_name: str, keys: list) -> list:
    with open(file_name, "r") as pop_stats: 
        data = json.load(pop_stats)
    return [[record[k] for record in data] for k in keys]

keys = ["pop2023", "pop2020", "growth", "name", "aland_sqmi", "intptlat", "intptlong", "slug", "usps", "lng", "lat", "rank", "density"]
# print(read_data("population.json", keys))

def stats(an_array: list) -> dict: 
    count = 0
    for num in an_array:
        count += num
    arr_stats = {
        'min': min(an_array), 
        'max': max(an_array),
        'range': max(an_array) - min(an_array),
        'mean': count / len(an_array),
        'mode': stat.mode(an_array),
        'var': stat.variance(an_array),
        'stdev': stat.stdev(an_array)
    }
    return arr_stats

# print(stats([1, 2, 3, 4, 5, 6, 7, 8]))


def print_stats(file_name: str):
    lists = read_data(file_name, keys)

    pop_values_raw = [v for v in lists[0] if v >= 10000]
    pop_row = stats(pop_values_raw)
    gr_row = stats(lists[2])
    den_row = stats(lists[-1])

    labels = ["population", "growth", "density"]
    columns = list(pop_row.keys())

    df = pd.DataFrame([pop_row, gr_row, den_row], index=labels)[columns]
    print(tabulate(df, headers="keys", tablefmt="grid", showindex=True))

# print_stats("population.json")