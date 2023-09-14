from testimport import *


x = input("Choose the following items. A(235), B(109), C(160) or D(35): ")
money_owed = money_owed_func(x)
return_money = loop(money_owed)

print("return ", return_money)


