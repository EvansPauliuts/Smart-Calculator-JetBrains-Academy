# write your code here
import re
import string

from abc import ABC
from operator import add, sub, mul, truediv


class MyException(Exception, ABC):
    pass


class Calculator:
    """ The program computes operations containing additions and subtractions """

    OPERATORS = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    commands = ['/help', '/exit']

    def __init__(self):
        self.process_replace = []
        self.data_dict = {}

    @staticmethod
    def execute_command(command):
        if command == '/exit':
            print('Bye!')
            return False
        elif command == '/help':
            print(Calculator.__doc__)

        return True

    def process_operator(self, operator):
        while operator.count('--') >= 1 or operator.count('++') >= 1:
            operator = operator.replace('--', '+')
            operator = operator.replace('++', '+')
            operator = operator.replace('+-', '-')
            operator = operator.replace('-+', '-')

        self.process_replace = operator.split(' ')

    def operator_result(self):
        number_rs = 0
        option = add
        str_operators_num = ' '.join(self.process_replace)

        if len(self.data_dict) != 0:
            for i in range(len(self.process_replace)):
                if self.process_replace[i] in self.data_dict:
                    self.process_replace[i] = self.data_dict[self.process_replace[i]]

        try:
            if bool(re.match(r'[+-/*]?\w+[+-/*]|\w+[^0-9\s+]', str_operators_num)):
                raise MyException('Invalid identifier')
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
    def substring_list(name):
        val, num = ''.join(name.split()).replace('=', ' ').split()
        return val, num

    def save_dict_hash(self, val):
        val, num = self.substring_list(val)

        try:
            if True in [num.endswith(v) for v in string.ascii_lowercase]:
                raise MyException('Invalid identifier')

            self.data_dict[val] = num

        except MyException as e:
            print(e.args[0])

    def check_dict_hash(self, val):
        a, b = self.substring_list(val)

        if b in self.data_dict:
            self.data_dict[a] = self.data_dict[b]
        else:
            print('Unknown variable')

    def check_dict(self, name):
        if name in self.data_dict:
            print(self.data_dict[name])
        else:
            print('Unknown variable')


def main():
    calculator = Calculator()
    flag = True

    while flag:
        user_calc = input()

        try:
            if user_calc.startswith('/'):
                if user_calc in Calculator.commands:
                    flag = Calculator.execute_command(user_calc)
                    continue
            elif user_calc == '':
                continue
            elif bool(re.match(r'^[a-z]+(\s?)+?=(\s?)+?\d+', user_calc)) and user_calc.count('=') == 1:
                calculator.save_dict_hash(user_calc)
                continue
            elif bool(re.match(r'\s*?\w+(\s?)+?=(\s?)+?[a-z]', user_calc)):
                calculator.check_dict_hash(user_calc)
                continue
            elif bool(re.match(r'\w+$', user_calc)):
                calculator.check_dict(user_calc)
                continue
            elif user_calc.count('=') >= 2:
                print('Invalid assignment')
                continue

            calculator.process_operator(user_calc)
            calculator.operator_result()
        except (ValueError, TypeError):
            print('Unknown command')


if __name__ == '__main__':
    main()
