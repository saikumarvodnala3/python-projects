import datetime

product_catalog = {}

shopping_cart = {}

customer_name = input("Enter your name: ")
customer_email = input("Enter your email: ")
customer_number = input("Enter your customer number: ")
current_date = datetime.date.today()

def generate_invoice_number():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    invoice_number = f"INV-{timestamp}"
    return invoice_number
def add_to_catalog():
    item_id = input("Enter item ID: ")
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    product_catalog[item_id] = {'name': item_name, 'price': item_price}
    print(f"Item '{item_name}' added to the catalog.")

def add_to_cart():
    item_id = input("Enter item ID to add to the cart: ")
    if item_id in product_catalog:
        quantity = int(input("Enter quantity: "))
        if item_id in shopping_cart:
            shopping_cart[item_id]['quantity'] += quantity
        else:
            shopping_cart[item_id] = {
                'name': product_catalog[item_id]['name'],
                'price': product_catalog[item_id]['price'],
                'quantity': quantity
            }
        print(f"{quantity} {product_catalog[item_id]['name']} added to the cart.")
    else:
        print("Invalid item ID. Please select a valid item from the catalog.")

def calculate_total():
    total_amount = 0.0

    for item_id, item_info in shopping_cart.items():
        item_price = item_info['price']
        item_quantity = item_info['quantity']
        item_total = item_price * item_quantity
        total_amount += item_total

    return total_amount

def generate_bill():
    total_amount = calculate_total()

    print("\n*** E-commerce Invoice ***")
    print(f"Customer Name: {customer_name}")
    print(f"Customer Email: {customer_email}")
    print(f"Customer Number: {customer_number}")
    print(f"Invoice Number: {invoice_number}")
    print(f"Date: {current_date}")
    print("\nItem\t\tQuantity\tPrice\t\tTotal")
    print("-" * 50)

    for item_id, item_info in shopping_cart.items():
        item_name = item_info['name']
        item_price = item_info['price']
        item_quantity = item_info['quantity']
        item_total = item_price * item_quantity
        print(f"{item_name}\t\t{item_quantity}\t\t${item_price:.2f}\t\t${item_total:.2f}")

    print("-" * 50)
    print(f"Subtotal: ${total_amount:.2f}")
    print("Thank you for shopping!")

while True:
    print("\nMenu:")
    print("1. Add item to catalog")
    print("2. Add item to cart")
    print("3. Generate invoice")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_to_catalog()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        # Generate a new invoice number before generating the invoice
        invoice_number = generate_invoice_number()
        generate_bill()
        break
    elif choice == '4':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please select a valid option.")