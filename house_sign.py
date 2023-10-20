#PROMPT
"""
Mark Daniels is a carpenter who creates personalized house signs. He wants an application to compute the price of any sign a customer orders, based on the following factors:
a. The minimum charge for all signs is PHP 300.
b. If the sign is made of oak, add PHP 150. No charge is added for pine.
c. The first six letters or numbers are included in the minimum charge; there is PHP 30 charge for each additional character.
d. Black or white characters are included in the minimum charge; there is an additional PHP 120 charge for gold.
Draw a flowchart and pseudocode that accepts data for an order number, customer name, wood type, number of characters and color of characters. Display the final price for the sign.
"""


import random

def formatName(firstName, middleName, lastName):
    middle_initial = middleName[0]
    format_name = (f"{firstName} {middle_initial}. {lastName}")
    return format_name

def generate_random_number():
    random_digits = [str(random.randint(0, 9)) for _ in range(12)]
    random_number = "".join(random_digits[:4]) + "-" + "".join(random_digits[4:8]) + "-" + "".join(random_digits[8:12])
    return random_number

#print complete details of customer and breakdown of total
def displayDetails():
    customer_formatted_name = formatName(customer_first_name, customer_middle_name, customer_last_name)
    customer_order_number = generate_random_number()
    print("---Order Submitted---")
    print("---Order Details---")
    print(f"Order Number: {customer_order_number}")
    print(f"Customer Name: {customer_formatted_name}")
    if wood_type == "O":
        print("Wood Type: Oak Wood")
    else:
        print("Wood Type: Pine Wood")
    print(f"Customer Word: {customer_word}")
    if word_color == "B":
        print("Color: Black and White")
    else:
        print("Color: Gold")
    print(f"Total price is ₱{round((total_price * 1.05), 0)}.")

def displayBreakdown():
    print(f"Base Fare: ₱{base_charge}")
    # wood_type == "O" and 
    if isOak == True:
        print(f"Wood Type: {wood_type}ak - ₱150")
    elif isPine == True:
        print(f"Wood Type: {wood_type}ine - ₱0")
    else:
        pass
    
    if iswordExceeded == True:
        print(f"Customer Word: {customer_word} - {word_len} letters - ₱{add_char_total}")
    elif iswordNotExceeded == True:
        print(f"Customer Word: {customer_word} - {word_len} letters - ₱0")
    else:
        pass

    if isColorGold == True:
        print(f"Word Color: {word_color}old - ₱120")
    elif isColorBW == True:
        print(f"Word Color: {word_color}lack and White - ₱0")
    
    print(f"Subtotal: ₱{total_price}")
    print("VAT Rate - 5%")
    print(f"Total Amount: ₱{round((total_price * 1.05), 0)}")

print("Welcome to Mark Daniel's Personalized House Signs!")
customer_first_name = input("Enter first name: ").title()
customer_middle_name = input("Enter middle name: ").title()
customer_last_name = input("Enter last name: ").title()

wood_type = input("Oak Wood - Additional P150 \nPine Wood - Free \nEnter wood type (O for oak, P for pine): ").upper()
customer_word = input("Enter preferred word to be house sign: ").title()
word_len = len(customer_word)
word_color = input("Enter color (Black and White (B), or Gold (G)): ").upper()

base_charge = 300
total_price = 300
isOak = False
isPine = False
iswordExceeded = False
iswordNotExceeded = False
isColorGold = False
isColorBW = False

if wood_type == "O":
    total_price = total_price + 150
    isOak = True
elif wood_type == "P":
    isPine = True
else:
    print("Invalid choice")
    exit

if word_len > 6:
    iswordExceeded = True
    additional_char = word_len - 6
    add_char_total = additional_char * 30
    total_price = total_price + add_char_total
elif word_len < 6:
    iswordNotExceeded = True
else:
    pass

if word_color == "G":
    isColorGold = True
    total_price = total_price + 120
elif word_color == "B":
    isColorBW = True
else:
    pass

displayDetails()
seeBreakdown = input("Do you want to see breakdown (Y/N)? ").upper()

if seeBreakdown == "Y":
    displayBreakdown()
else:
    exit
