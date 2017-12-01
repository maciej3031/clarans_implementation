import argparse
import random

from utils import plot_data, read_from_file

random.seed()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--filename', help='Input file name. Default = data.txt.', default='data.txt')
    args = p.parse_args()

    points = read_from_file(args.filename)
    plot_data(points)
