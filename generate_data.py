import argparse
import random

from utils import plot_data, read_from_file

random.seed()


def generate_data(filename):
    with open(filename, 'w+') as f:
        for j in range(0, 40, 8):
            for i in range(100):
                x = random.randrange(j * 100, j * 100 + 800, 1)
                y = random.randrange(j * 100, j * 100 + 800, 1)
                point = "{} {}\n".format(x, y)
                f.write(point)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--filename', help='Output file name.', default='data.txt')
    args = p.parse_args()

    generate_data(args.filename)
    print('Data saved to file {}'.format(args.filename))

    points = read_from_file(args.filename)
    plot_data(points)
