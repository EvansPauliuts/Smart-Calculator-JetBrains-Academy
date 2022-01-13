# write your code here
import re

from abc import ABC
from operator import add, sub, mul, truediv


class MyException(Exception, ABC):
    pass


class Calculator:
    OPERATORS = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    def __init__(self):
        self.process_replace = []

    def process_operator(self, operator):
        while operator.count('--') >= 1 or operator.count('++') >= 1:
            operator = operator.replace('--', '+')
            operator = operator.replace('++', '+')
            operator = operator.replace('+-', '-')

        self.process_replace = operator.split(' ')

    def operator_result(self):
        number_rs = 0
        option = add
        str_operators_num = ' '.join(self.process_replace)

        try:
            if bool(re.match(r'[+-/*]?\w+[+-/*]|\w+[^0-9\s+]', str_operators_num)):
                raise MyException('Invalid expression')
            else:
                for item in self.process_replace:
                    if item in Calculator.OPERATORS:
                        option = Calculator.OPERATORS[item]
                    else:
                        number = int(item)
                        number_rs = option(number_rs, number)

                print(number_rs)
        except MyException as e:
            print(e.args[0])

    @staticmethod
    def help():
        print('The program computes operations containing additions and subtractions')


def main():
    calculator = Calculator()

    while True:
        user_calc = input()

        try:
            if user_calc == '/exit':
                print('Bye!')
                break
            elif not user_calc:
                continue
            elif user_calc == '/help':
                calculator.help()
                continue

            calculator.process_operator(user_calc)
            calculator.operator_result()
        except (ValueError, TypeError):
            print('Unknown command')


if __name__ == '__main__':
    main()
