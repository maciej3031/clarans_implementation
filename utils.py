import os

import matplotlib.pyplot as plt

from model import Point


def write_to_file(filename, points):
    with open(os.path.join('data', filename), 'w+') as f:
        for num, pnt in enumerate(points):
            f.write("{} {} {}\n".format(pnt.x, pnt.y, pnt.cluster))


def read_from_file(filename):
    with open(os.path.join('data', filename), "r") as f:
        points = []
        for coordinates in f.readlines():
            point = Point(*[int(i) for i in coordinates.split()])
            points.append(point)
    return points


def plot_data(points, medoids=None, clusters=False):
    if clusters:
        for med in medoids:
            indices_per_claster = [num for num, pnt in enumerate(points) if pnt.cluster == med]
            claster = [points[idx] for idx in indices_per_claster]
            plt.scatter(*zip(*[(pnt.x, pnt.y) for pnt in claster]))
    else:
        plt.scatter(*zip(*[(pnt.x, pnt.y) for pnt in points]))

    if medoids is not None:
        plt.scatter(*zip(*[(points[i].x, points[i].y) for i in medoids]), color='black')

    plt.show()
