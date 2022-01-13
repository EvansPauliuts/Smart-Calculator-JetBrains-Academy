# write your code here
import re


class Calculator:
    OPERATORS = (
        '-',
        '+',
        '/',
        '-'
    )

    def __init__(self):
        self.process_replace = []

    def process_operator(self, operator):
        while operator.count('--') >= 1 or operator.count('++') >= 1:
            operator = operator.replace('--', '+')
            operator = operator.replace('++', '+')
            operator = operator.replace('+-', '-')

        self.process_replace = operator.split(' ')

    def operator_result(self):
        str_operators_num = ''.join(self.process_replace)
        sum_result = sum(map(int, re.findall(r'[+-/*]?\d+', str_operators_num)))
        print(sum_result)

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
            pass


if __name__ == '__main__':
    main()
