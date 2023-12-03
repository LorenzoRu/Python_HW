nb1 = int(input())
nb2 = int(input())
operator = input()
def calculator(nb1, nb2, operator):
        if operator == '+':
            result = nb1 + nb2
        elif operator == '-':
            result = nb1 - nb2
        elif operator == '*':
            result = nb1 * nb2
        elif operator == '/':
            result = nb1 / nb2
        elif operator == '//':
            result = nb1 // nb2
        elif operator == '%':
            result = nb1 % nb2
        elif operator == '**':
            result = nb1 ** nb2
        else:
            return None
        return result
result = calculator(nb1, nb2, operator)
if result is not None:
    print(result)