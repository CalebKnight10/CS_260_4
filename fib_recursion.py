#  fib's index  0 1 2 3 4 5 6 7 etc
#  Fibonacci is 0 1 1 2 3 5 8 13 etc

def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num - 2)


def main():
    print("The fibonacci sequence for 4  is: ", fib(4))
    print("The fibonacci sequence for 10  is: ", fib(10))
    print("The fibonacci sequence for 33  is: ", fib(33))


if __name__ == '__main__':
    main()

