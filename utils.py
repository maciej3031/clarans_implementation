import os
import random

import matplotlib.pyplot as plt
from colour import Color

from model import Point, Polygon


def write_to_file(filename, objects, polygons=False):
    with open(os.path.join('data', filename), 'w+') as f:
        for num, obj in enumerate(objects):
            if polygons:
                f.write("{} {}\n".format(obj.vertices, obj.cluster))
            else:
                f.write("{} {} {}\n".format(obj.x, obj.y, obj.cluster))


def read_from_file(filename, polygons=False):
    with open(os.path.join('data', filename), "r") as f:
        objects = []
        for coordinates in f.readlines():
            if polygons:
                list_of_pairs = list(zip(*[iter([int(i) for i in coordinates.split()])] * 2))
                polygons = Polygon(vertices=[Point(x, y) for x, y in list_of_pairs])
                objects.append(polygons)
            else:
                point = Point(*[int(i) for i in coordinates.split()])
                objects.append(point)
    return objects


def plot_info(medoids, objects):
    print('\nSuccess!')
    print("Medoids found:")
    for i in medoids:
        print(objects[i])


def plot_data(objects, medoids=None, clusters=False, polygons=False):
    if clusters:
        _plot_clusters(objects, medoids, polygons=polygons)
    else:
        _plot_all(objects, polygons=polygons)

    if medoids is not None:
        _plot_medoids(objects, medoids, polygons=polygons)

    plt.show()


def _plot_clusters(objects, medoids, polygons=False):
    red = Color("red")
    blue = Color("blue")
    colors = [i.hex_l for i in red.range_to(blue, len(medoids))]
    random.shuffle(colors)
    for num, med in enumerate(medoids):
        indices_per_claster = [num for num, pol in enumerate(objects) if pol.cluster == med]
        claster = [objects[idx] for idx in indices_per_claster]
        if polygons:
            for pol in claster:
                plt.plot([pnt.x for pnt in pol.vertices], [pnt.y for pnt in pol.vertices], color=colors[num])
        else:
            plt.scatter([pnt.x for pnt in claster], [pnt.y for pnt in claster], color=colors[num])


def _plot_all(objects, polygons=False):
    if polygons:
        for obj in objects:
            plt.plot([pnt.x for pnt in obj.vertices], [pnt.y for pnt in obj.vertices], color='darkblue')
    else:
        plt.scatter([pnt.x for pnt in objects], [pnt.y for pnt in objects], color='darkblue')


def _plot_medoids(objects, medoids, polygons=False):
    if polygons:
        for med in medoids:
            plt.plot([pnt.x for pnt in objects[med].vertices], [pnt.y for pnt in objects[med].vertices], color='black')
    else:
        plt.scatter([objects[i].x for i in medoids], [objects[i].y for i in medoids], color='black')
