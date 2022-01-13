# write your code here


class Calculator:
    def __init__(self):
        self.nums = []

    def input_value(self):
        num_list = input().split()
        self.nums = [int(m) for m in num_list]

    def add(self):
        print(sum(self.nums))


def main():
    calculator = Calculator()
    calculator.input_value()
    calculator.add()


if __name__ == '__main__':
    main()
