'''
Kevin Collura
Professor Eckert
CS 175L
Stocks
'''
#Inputs
numShares=int(input('How many shares did you purchase? '))
stockSoldFor=float(input('Amount the stock sold for:$ '))
purchaseCommission=float(input('Commission paid on the purchase:$  '))
sellingCommission=float(input('Commission paid on the sale:$ '))
purchasePrice=float(input('Amount paid for the stock:$ '))
#Calculations
amountPaidForStock=numShares*purchasePrice
totalPaid=amountPaidForStock+purchaseCommission
purchaseCommission=commissionRate*purchasePrice
stockSoldFor=numShares*sellingprice
sellingCommission=commissionRate*stockSoldfor
totalRecieved=stockSoldFor-sellingCommission
profitOrLoss=totalRecieved-totalPaid

#Print Statements
print('Amount paid for the stock:$ ', amountPaidForStock)
print('Commission paid on the purchase:$ ', purchaseCommission)
print('Amount the stock sold for:$ ', stockSoldFor)
print('Commission paid on the sale:$ ', sellingCommission)
print('Profit(or loss if negative):$ ',profitOrLoss)
