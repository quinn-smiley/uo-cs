import csv
import math
import random

import matplotlib.pyplot as plt


COLUMN_TITLES = ["Labs", "Projects", "Exams"]


def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    with open(filename, "r") as file:
        csv_read = csv.reader(file)
        header = next(csv_read)

        col_indices = [header.index(title) for title in column_titles]

        result = {}
        row_number = 0

        for row in csv_read:
            row_values = []
            for col in col_indices:
                cell_text = row[col]
                cell_number = float(cell_text)
                row_values.append(cell_number)

            result[row_number] = tuple(row_values)
            row_number += 1

        return result

def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Euclidean distance between two points represented as tuples.

    Listing 7.1 in PPC, with modifications for compliance to PEP 8.

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).
    """
    x_val_sq = (point1[0] - point2[0]) ** 2
    y_val_sq = (point1[1] - point2[1]) ** 2
    result = round(math.sqrt(x_val_sq + y_val_sq), 2)
    return result

def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until
    you have k unique centroids.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    data_points = list(data.values())

    result = random.sample(data_points, k)
    return result


def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> tuple:
    """Create clusters using the k-means algorithm.

    From Listing 7.8, modified to comply with PEP 8.

    Args:
        k: How many clusters to create.
        centroids: The list of centroids, one per cluster.
        data: Dictionary mapping row number -> point tuple.
        repeats: How many iterations to run.

    Returns:
        tuple[list, list]: (clusters, centroids) where clusters is a list of
        lists of points and centroids is the final list of centroid points.
    """
    for _ in range(repeats):
        clusters = [[] for _ in range(k)]
        for point in data.values():
            least_dist = euclid_dist(point, centroids[0])
            closest = 0
            for i in range(1, k):
                d = euclid_dist(point, centroids[i])
                if d < least_dist:
                    least_dist = d
                    closest = i
            clusters[closest].append(point)
        new_cen = []
        for cluster in clusters:
            if not cluster:
                new_cen.append(centroids[len(new_cen)])
            else:
                n = len(cluster[0])
                avg_coords = []
                for i in range(n):
                    coord_sum = sum(p[i] for p in cluster)
                    avg_coords.append(coord_sum / len(cluster))
                new_cen.append(tuple(avg_coords))
        centroids = new_cen
    return clusters, centroids


def visualize_clusters(
    dataset_name: str, titles: list, clusters: list, centroids: list
) -> plt.Figure:
    """OPTIONAL - Extra credit
    Visualize the clusters and centroids. Use a different color for each cluster.
    Args:
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    pass


def main():
    """Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {
        ("earthquakes", ("latitude", "longitude")): 5,
        ("earthquakes", ("depth", "mag")): 5,
        ("cis210_scores", ("Projects", "Exams")): 5,
    }
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f"\nDataset: {dataset} {titles}")
        # Part 8.1
        data = load_numerical_data(dataset + ".csv", column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")

        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")


if __name__ == "__main__":
    main()
