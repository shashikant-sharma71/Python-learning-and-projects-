menu={
    'Pizza':100,
    'Pasta':40,
    'Salad':10,
    'Burgur':30,
    'Coffee':30
}
print("Welcome To our Restraunt")
print("pizza:Rs 50\n""pasta:Rs 40\n""Salad:Rs 10\n""Burgur:Rs 30\n")

order_total=0

item_1=input(" Please Enter the name of item you want to order")
if item_1 in menu:
    order_total+=menu[item_1]
    print("Your order{item_1} has been added to your order")
else:
    print("Order item{item_1}is not available yet!")

another_order=input("Do you want to add another item")
if another_order =='yes':
    item_2=input("Enter the item")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Your order{item_2} has been added to your order")
else:
    print("Order item{item_2}is not available yet!")

print("The total amount you have to pay is",order_total)