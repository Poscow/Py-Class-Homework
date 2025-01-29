muffins = 10
cupcakes = 10
while True:
    if muffins > 0 and cupcakes > 0:
        customer_input_2 = "Would you like to buy a muffin or a cupcake? "
    elif muffins > 0:
        customer_input_2 = "Would you like to buy a muffin? "
    elif cupcakes > 0:
        customer_input_2 = "Would you like to buy a cupcake? "
    else:
        all_out = print("All items are out of stock, come back tomorrow!")
        break
    customer_input = input(customer_input_2).lower()
    if customer_input == "no":
        break
    if customer_input == "muffin":
        if muffins > 0:
            muffins -= 1
            print(f"{muffins} muffins left")
        else:
            print("Out of stock")
    elif customer_input == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
            print(f"{cupcakes} cupcakes left")
        else:
            print("Out of stock")
    else:
        print("Please enter 'muffin', 'cupcake', or 'no'.")
print(f"muffins: {muffins} cupcakes: {cupcakes}")
