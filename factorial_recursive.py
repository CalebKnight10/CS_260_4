#  A factorial is multiplying our num by the numbers before it
# Ex, 5 would be 5x4x3x2x1


def factorial(num):
    if num <= 1:
        return num
    else:
        return factorial(num - 1) * num


def main():
    print(factorial(9))


if __name__ == '__main__':
    main()
