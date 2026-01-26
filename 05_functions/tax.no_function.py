## tax.no_function.py

# Rewrite the tax.no_function.py module using a function for get_inputs()
def get_inputs():
    return input(f'Enter Q for quit or any other key to compute tax ').upper()


# Rewrite the tax.no_function.py module using a function for calculate_price_with_tax()
def calculate_price_with_tax(price, tax):
    calculated_price = price * (100 + tax) / 100
    print(f'The calculated price is {calculated_price}')


done = False
while not done:
    if (sentinel := get_inputs()) == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    calculate_price_with_tax(price, tax)