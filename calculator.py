# write your code here


class Calculator:
    def __init__(self):
        self.nums = []

    def input_value(self):
        num_list = input().split()
        self.nums = num_list
        return num_list

    def add(self):
        print(sum([int(v) for v in self.nums]))


def main():
    calculator = Calculator()

    while True:
        name = calculator.input_value()

        try:
            str_value = ''.join(name)

            if str_value == '/exit':
                print('Bye!')
                break
            elif str_value == '':
                continue
            else:
                calculator.add()
                continue
        except (ValueError, TypeError):
            pass


if __name__ == '__main__':
    main()
