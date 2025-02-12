def deposit():
    running = True
    while running:
        amount = input("What would you like to deposit? $")
        
        if amount.isdigit(): #positive numbers
            amount = int(amount)

            if amount > 0: #check if amount is bigger than zero
                running = False
    return None
deposit()
a = 3
print("Aaa")

