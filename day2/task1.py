import numpy as np


def is_safe_report(levels):
    diffs = np.diff(levels)

    increasing = np.all(diffs > 0)
    decreasing = np.all(diffs < 0)
    if not (increasing or decreasing):
        return False

    diffs = np.abs(diffs)

    return np.all(np.logical_and((diffs > 0), (diffs < 4)))


def solution(lines):

    safe_reports = 0

    for report in lines:
        levels = np.asarray([int(level) for level in report.split()],
                            dtype=np.int64)
        safe_reports += is_safe_report(levels)

    print(safe_reports)


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    solution(lines)
