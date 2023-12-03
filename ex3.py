K0 = int(input())
n = int(input())
i = int(input())
def capital_calculator(K0, i, n):
    if n == 0:
        return K0
    else:
        return int(K0 * (1 + i/100) ** n)
capital = capital_calculator(K0, i, n)
print(capital)