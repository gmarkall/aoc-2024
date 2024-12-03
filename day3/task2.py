import re


def solution(data):
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)|don\'t|do", data)

    enabled = True
    total = 0
    for match in matches:
        if match == "do":
            enabled = True
        elif match == "don't":
            enabled = False
        else:
            if enabled:
                x, y = match[4:-1].split(",")
                total += int(x) * int(y)

    print(total)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    solution(data)
