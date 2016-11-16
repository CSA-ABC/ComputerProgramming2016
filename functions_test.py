#Elijah Mitchell
#10/4/16
#period 2
def total(price,Number_of_items,tax):
    items_cost=price*Number_of_items
    tax_total=items_cost*tax
    total_cost=items_cost+tax_total
    return total_cost
num=int(input("Types of items: "))
TOTAL_PRICE=0.0

for i in range(num):
    x=float(input("Price: "))
    y=int(input("How many: "))
    z=float(input("Tax rate: "))*.01
    owed=total(x,y,z)
    TOTAL_PRICE+=owed

print(TOTAL_PRICE)
