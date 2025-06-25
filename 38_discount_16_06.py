#calculate the find price after the discount 
#input=150 discount=20% output=120

price = float(input("Enter the original price: "))

discount = float(input("Enter the discount percentage: "))

discountamount = (discount / 100) * price

finalprice = price - discountamount

print("Final price after discount:", finalprice)

    