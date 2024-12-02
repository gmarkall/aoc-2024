import numpy as np


def solution(lines):
    left = []
    right = []

    for line in lines:
        x, y = line.split()
        x = x.strip()
        y = y.strip()
        x = int(x)
        y = int(y)
        left.append(x)
        right.append(y)

    left = np.asarray(sorted(left), dtype=np.int64)
    right = np.asarray(sorted(right), dtype=np.int64)

    total = np.sum(np.abs(right - left))

    print(total)


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    solution(lines)
