import statistics
import matplotlib.pyplot as plt

# def read_data(file_name: str) -> list:
#     total = []
#     with open(file_name) as rain_file:
#         for a_line in rain_file: 
#             a_line = a_line.strip()
#             values = a_line.split(",")
#             total.append((values[0], values[1]))
#     return total

def read_data(file_name: str) -> list:
    with open(file_name) as rain_file: 
        return [
            tuple(part.strip() for part in line.split(","))
            for line in rain_file
        ]
    
# print(read_data("november_rain.csv"))

# def list_to_dict(a_list: list) -> dict:
#     d = {}
#     for pair in a_list:
#         average = pair[1]
#         year = pair[0][:4]
#         d[year] = average
#     return d

def list_to_dict(a_list: list) -> dict:
    return {
        int(pair[0][:4]) : float(pair[1]) for pair in a_list
    }

# print(list_to_dict(read_data("november_rain.csv")))

# def dict_to_list(a_dict: dict) -> list: 
#     final = []
#     for year in a_dict: 
#         average = a_dict[year]
#         final.append((year, average))
#     return final

def dict_to_list(a_dict: dict) -> list: 
    return [
        (year, a_dict[year]) for year in a_dict
    ]

# print(dict_to_list(list_to_dict(read_data("november_rain.csv"))))

def mean_rainfall(values: list) -> float: 
    avgs = []
    for pair in values: 
        avgs.append(pair[1])
    return statistics.mean(avgs)

# print(mean_rainfall(dict_to_list(list_to_dict(read_data("november_rain.csv")))))

raw = read_data("november_rain.csv")
data_dict = list_to_dict(raw)

abscissas = sorted(data_dict.keys())
ordinates = [data_dict[y] for y in abscissas]

overall_mean = statistics.mean(ordinates)

plt.plot(abscissas, ordinates, 'rx')
plt.axhline(overall_mean, linestyle=':', color='gray')
plt.ylabel('Average Monthly Rainfall')
plt.xlabel('Year')
plt.title('Average Monthly Rainfall by Year')
plt.show()


def high_rain_years() -> list:
    values = dict_to_list(list_to_dict(read_data("november_rain.csv")))
    m = mean_rainfall(values)
    return [(year) for (year, avg) in values if avg >= 1.5 * m]

# print(high_rain_years())


def percentage_increase() -> None:
    data_dict = list_to_dict(read_data("november_rain.csv"))
    values = dict_to_list(data_dict)
    m = mean_rainfall(values)

    qualifying_years = [year for (year, avg) in values if avg >= 1.5 * m]

    with open("out.txt", "w") as f:
        for year in sorted(qualifying_years):
            avg = data_dict[year]
            pct_increase = ((avg - m) / m) * 100.0
            f.write(
                f"Year: {year}, "
                f"Average Rainfall in Inches: {avg:.2f}, "
                f"Percentage Increase Over Mean: {pct_increase:.2f}%\n"
            )

percentage_increase()