import matplotlib.pyplot as plt
import csv

def read_data(file_name):
    with open(file_name, "r") as f:
        csv_read = csv.reader(f)
        header = next(csv_read)
        print(header)
        dict = {
            (line[0], line[2]): {
                header[index]: line[index]
                for index in range(3, len(line))
            }
            for line in csv_read
        }
    return dict

# print(read_data("city-scores.csv"))

def create_total_score(data_dict):
    for key in data_dict:
        inner = data_dict[key]
        total = 0.0
        for value in inner.values():
            total = total + float(value)
        inner["Total Score"] = total
    return data_dict

# print(create_total_score(read_data("city-scores.csv")))

# define auxiliary functions here

def plot_data(data_dict):
    housing = []
    cofl = []
    for key, scores in data_dict.items():
        h = float(scores['Housing'])
        c = float(scores['Cost_of_Living'])

        housing.append(h)
        cofl.append(c)

    plt.scatter(housing, cofl, color = 'red', marker = 'x')

    plt.xlabel("Housing")
    plt.ylabel("Cost of Living")

    plt.savefig("housing.png")
    
    plt.grid(True)
    plt.show()

print(plot_data(read_data("city-scores.csv")))
# if __name__ == "__main__":
#     # the main conditional execution