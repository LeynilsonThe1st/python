""" __author__: Leynilson José "Snake" """
# LED | accepted


def countLeds(s: str):
    if s == '1':
        return 2
    elif s in ('3', '2', '5'):
        return 5
    elif s == '4':
        return 4
    elif s in ('0', '6', '9'):
        return 6
    elif s in '7':
        return 3
    elif s in '8':
        return 7


def getTotalLeds(number: str):
    total = 0
    for n in number:
        total += countLeds(n)
    return total


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        print(getTotalLeds(n), "leds")


if __name__ == "__main__":
    main()
