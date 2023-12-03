price = int(input())
amount_given = int(input())

def given_back (price, amount_given):
    rest = amount_given - price
    bills_100 = rest // 100
    rest %=100
    bills_10 = rest // 10
    rest %=10 
    coins_2 =  rest // 2
    rest %=2
    coins_1 = rest
    cash =bills_100 + bills_10 + coins_2 + coins_1
    return cash

print(given_back(price, amount_given))