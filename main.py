print("Welcome to the GC Fruit Market!")
print("What is your name?")
shopper_name = input("> ")
question_txt = f"Welcome {shopper_name}. Which Fruit would you like to buy?"
subtotal_cost = int(0)
total_apples = int(0)
total_grapes = int(0)
total_oranges = int(0)
fruits = ["Apple", "Grape", "Orange"]
continue_txt = f"Would you like to buy another piece of fruit? y/n"
continue_shopping = "y"

while True:
    if continue_shopping == "y":
        print(question_txt)
        print(f"1. {fruits[0]} $2")
        print(f"2. {fruits[1]} $2")
        print(f"3. {fruits[2]} $3")
        choice = input("> ")
        index = int(choice) - 1
        if choice == "1":
            item_cost = int(2)
            total_apples += 1
        elif choice == "2":
            item_cost = int(1)
            total_grapes += 1
        else:
            item_cost = int(3)
            total_oranges += 1

        subtotal_cost += item_cost

        print(f"You bought 1 {fruits[index]} at ${item_cost}")
        print(continue_txt)
        continue_shopping = input("> ")
    else:
        break

print(f"Order for {shopper_name}")
print(f"{total_apples} apple(s) at $2 apiece")
print(f"{total_grapes} grape(s) at $1 apiece")
print(f"{total_oranges} orange(s) at $3 apiece")
print(f"Subtotal: ${subtotal_cost}")
tax_cost = round(subtotal_cost * .05, 2)
print(f"5% Tax: ${tax_cost}")
total_cost = subtotal_cost + tax_cost
print(f"Total: ${total_cost}")

