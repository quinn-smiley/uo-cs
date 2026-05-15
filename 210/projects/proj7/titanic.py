import titanic
import csv
import statistics as stat
import matplotlib.pyplot as plt
# Write your functions here

def load_data(file_name: str, types: dict) -> dict:
    with open(file_name, "r") as file:
        csv_read = csv.reader(file)
        header = next(csv_read)

        result = {}
        for col in types:
            result[(col, types[col])] = []

        for row in csv_read:
            for i in range(len(header)):
                col = header[i]
                if col in types and i < len(row):
                    value = types[col](row[i])
                    result[(col, types[col])].append(value)

    return result

titanic_types = {
    'PassengerId': int,
    'Survived': int,
    'Pclass': int,
    'Sex': str,
    'Age': float,
    'SibSp': int,
    'Parch': int,
    'Fare': float,
    'Embarked': str,
    'FamilySize': int,
    'age_group': str
}

print(load_data("titanic_clean.csv", titanic_types))
data = load_data('titanic_clean.csv', titanic_types)
# for key, val in data.items():
#     print(key, val[:4])

def unique_count(column_values):
    seen = []
    for item in column_values:
        if item not in seen:
            seen.append(item)
    return len(seen)


def most_frequent(column_values):
    counts = {}
    for item in column_values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    max_count = 0
    result = None
    for item, c in counts.items():
        if c > max_count:
            max_count = c
            result = item
    return result


def summarize(data: dict):
    for key, values in data.items():
        col_name = key[0]   # e.g. 'Age'
        col_type = key[1]   # e.g. int or float
        if not values:
            continue

        if col_type in (int, float):
            col_min = round(min(values), 1)
            col_max = round(max(values), 1)
            n = len(values)
            mean = round(sum(values) / n, 1)
            mode = round(stat.mode(values), 1)
            stdev = round(stat.stdev(values), 1)
            print(f"\nStatistics for {col_name}:")
            print(f"  min:    {col_min}")
            print(f"  max:    {col_max}")
            print(f"  mean:   {mean}")
            print(f"  stdev:  {stdev}")
            print(f"  mode:   {mode}")

        else:
            print(f"\nStatistics for {col_name}:")
            print(f"  Number of unique values: {unique_count(values)}")
            print(f"  Most common value: {most_frequent(values)}")
        
# summarize(data)


def pearson_corr(x: list, y: list):
    if len(x) != len(y):
        print("Error: Lists must be the same length")
        return None
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    dev_x = [xi - mean_x for xi in x]
    dev_y = [yi - mean_y for yi in y]
    numerator = sum(a * b for a, b in zip(dev_x, dev_y))
    sum_sq_x = sum(a * a for a in dev_x)
    sum_sq_y = sum(b * b for b in dev_y)
    denominator = (sum_sq_x ** 0.5) * (sum_sq_y ** 0.5)
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 2)

# age_list = data[('Age', float)]
# survived_list = data[('Survived', int)]
# corr_age_survived = pearson_corr(age_list, survived_list)
# print(f'Correlation between age and survival: {corr_age_survived}')

# fare_list = data[('Fare', float)]
# corr_fare_survived = pearson_corr(fare_list, survived_list)
# print(f'Correlation between fare and survival: {corr_fare_survived}')

# family_list = data[('FamilySize', int)]
# corr_family_survived = pearson_corr(family_list, survived_list)
# print(f'Correlation between family size and survival: {corr_family_survived}')

def survivor_vis(data: dict, col_1: tuple, col_2: tuple) -> plt.Figure:
    x_data = data[col_1]
    y_data = data[col_2]
    survived = data[('Survived', int)]
    
    x_survived = []
    y_survived = []
    x_not_survived = []
    y_not_survived = []
    
    for i in range(len(survived)):
        if survived[i] == 1:
            x_survived.append(x_data[i])
            y_survived.append(y_data[i])
        else:
            x_not_survived.append(x_data[i])
            y_not_survived.append(y_data[i])

    figure = plt.figure(figsize=(8, 4))

    plt.scatter(x_not_survived, y_not_survived, marker='x', color='red', label='Did not survive')
    
    plt.scatter(x_survived, y_survived, marker='o', color='green', label='Survived')

    plt.xlabel(col_1[0])
    plt.ylabel(col_2[0])
    plt.title(f"Survival of Titanic Passengers")

    plt.legend()

    filename = f'scatter_{col_1[0]}_{col_2[0]}.png'
    plt.savefig(filename)

    plt.show(block=False)

# survivor_vis(data, ('Age', float), ('Fare', float))
# survivor_vis(data, ('Age', float), ('Pclass', int))
# survivor_vis(data, ('Age', float), ('Parch', int))


# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)

    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


# if __name__ == "__main__":
#     main()
