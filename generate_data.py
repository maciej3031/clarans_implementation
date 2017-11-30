import random

from utils import plot_data, read_data

random.seed()


def generate_data():
    with open('data.txt', 'w+') as f:
        for j in range(0, 32, 8):
            for i in range(100):
                x = random.randrange(j * 100, j * 100 + 800, 1)
                y = random.randrange(j * 100, j * 100 + 800, 1)
                point = "{} {}\n".format(x, y)
                f.write(point)


if __name__ == "__main__":
    generate_data()
    points = read_data()
    plot_data(points)
