import matplotlib.pyplot as plt


def write_to_file(filename, nodes, clusters):
    if len(nodes) != len(clusters):
        raise ValueError('Length of nodes and clusters does not match.')
    with open(filename, 'w+') as f:
        for i in range(len(nodes)):
            f.write("{} {} {}\n".format(nodes[i][0], nodes[i][1], clusters[i]))


def read_data():
    with open("data.txt", "r") as f:
        points = f.readlines()
        for j in range(len(points)):
            coordinates = points[j].split()
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            points[j] = tuple(coordinates)
    return points


def plot_data(points, medoids=None):
    plt.scatter(*zip(*points))
    if medoids is not None:
        plt.scatter(*zip(*[points[i] for i in medoids]))
    plt.show()
