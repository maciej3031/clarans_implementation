import argparse
import os
import random

from utils import plot_data, read_from_file

random.seed()


def generate_data(filename, clusters_number, number_of_objects, polygons=False):
    with open(os.path.join('data', filename), 'w+') as f:
        for m in range(5, clusters_number + 5):
            x = random.randrange(0, 300, 1) + random.randrange(100, 300, 1) * m
            y = random.randrange(0, 300, 1) + random.randrange(100, 300, 1) * m
            for i in range(int(number_of_objects / clusters_number)):
                r_plus_x = random.randrange(1, 400, 1)
                r_minus_x = random.randrange(1, 400, 1)
                r_plus_y = random.randrange(1, 400, 1)
                r_minus_y = random.randrange(1, 400, 1)
                xx = random.randrange(x - r_minus_x, x + r_plus_x, 1)
                yy = random.randrange(y - r_minus_y, y + r_plus_y, 1)
                if polygons:
                    vertices = []
                    for n in range(random.randrange(1, 10, 1)):
                        r_plus_xx = random.randrange(1, 100, 1)
                        r_minus_xx = random.randrange(1, 100, 1)
                        r_plus_yy = random.randrange(1, 100, 1)
                        r_minus_yy = random.randrange(1, 100, 1)
                        xxx = random.randrange(xx - r_minus_xx, xx + r_plus_xx, 1)
                        yyy = random.randrange(yy - r_minus_yy, yy+ r_plus_yy, 1)
                        vertices.append(str(xxx))
                        vertices.append(str(yyy))
                    polygon = " ".join(vertices) + "\n"
                    f.write(polygon)
                else:
                    point = "{} {}\n".format(xx, yy)
                    f.write(point)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--polygons', help='Use polygons instead of points.', action='store_true')
    p.add_argument('--filename', help='Output file name. Default = data.txt.', default='data.txt')
    p.add_argument('--clusters_number', help='Number of clusters. Default = 10.', default=10, type=int)
    p.add_argument('--objects_number', help='Number of objects. Default = 1000.', default=1000, type=int)
    args = p.parse_args()

    generate_data(args.filename, args.clusters_number, args.objects_number, args.polygons)
    print('Data saved to file {}'.format(args.filename))

    objects = read_from_file(args.filename, polygons=args.polygons)
    plot_data(objects, polygons=args.polygons)
