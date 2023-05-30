paid_amount = 0
while paid_amount < 50:
    print ("Amount Due: ", 50-paid_amount)
    payment = input("insert Coin: ")
    paid_amount = paid_amount + int(payment)
print ("Change Owed: ", paid_amount - 50)

