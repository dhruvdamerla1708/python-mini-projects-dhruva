def customer_info():
    name = input('Enter your customer name:')
    mobile_number = input('Enter mobile number:')
    return name, mobile_number

def get_grocery_items():
    n = int(input('Enter the number of items to be bought:'))
    items, quantity, price = [], [], []
    for i in range(n):
        a = input('Enter the name of the item:')
        items.append(a)
        b = int(input('Enter the quantity of the items:'))
        quantity.append(b)
        c = float(input('Enter the price of the item:'))
        price.append(c)
    return items, quantity, price

def calculate_bill():
    items, quantity, price = get_grocery_items()
    length, subtotal, total = len(items), [], 0
    for i in range(length):
        s = quantity[i] * price[i]
        subtotal.append(s)
        total += subtotal[i]
    final_amount = total
    if total >= 2000:
        discount = '15%'
        final_amount -= (total * 15) / 100
    elif 1000 <= total <= 1999:
        discount = '10%'
        final_amount -= (total * 10) / 100
    elif 500 <= total <= 999:
        discount = '5%'
        final_amount -= (total * 5) / 100
    else:
        discount = 'No Discount'
    return items, quantity, price, length, subtotal, total, discount, final_amount

def display_bill():
    name, mobile_number = customer_info()
    items, quantity, price, length, subtotal, total, discount, final_amount = calculate_bill()
    print(f'====== Grocery Bill======\nName: {name}\nMobile: {mobile_number}\n\n\nItems Purchased:')
    for i in range(length):
        print(f'{i+1}. {items[i]}: {quantity[i]}, Price: ${price[i]} -> Subtotal: ${subtotal[i]}')
    print(f'\n\n--------------------------------\nTotal: ${total}\nDiscount: {discount}\nFinal Amount: ${final_amount}\n\n===========================')

def main():
    display_bill()

main()
