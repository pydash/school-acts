base_bill = 0
total_bill = 0
month_with_31_days = [1, 3, 5, 7, 8, 10, 12]
month_with_30_days = [4, 6, 9, 11]
month_with_28_days = [2]

def get_package():
    while True:
        package_choices = ['A', 'B', 'C']
        package = input('Enter package (A/B/C): ').upper()
        if package in package_choices:
            return package
        else:
            continue

def get_month():
    while True:
        try:
            month = int(input('Enter month (1-12): '))
            if 1 <= month <= 12:
                return month
            else:
                print('Invalid number.')
                continue
        except ValueError:
            print('Invalid number. Try again.')
            continue

def get_hour(max_hour):
    while True:
        try:
            hour = int(input('Enter hours: '))
            if hour <= max_hour:
                return hour
            else:
                print('Invalid hour.')
                continue
        except ValueError:
            print('Wrong input. Try again.')
            continue

def package_a(base_bill):
    base_bill = base_bill + 200
    month = get_month()
    if month in month_with_31_days:
        while True:
            max_hour = 744
            hour = get_hour(max_hour)
            if hour < 11:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 10
                total_bill = (base_bill + (15 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break
    elif month in month_with_30_days:
        while True:
            max_hour = 720
            hour = get_hour(max_hour)
            if hour < 11:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 10
                total_bill = (base_bill + (15 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break
    elif month in month_with_28_days:
        while True:
            max_hour = 672
            hour = get_hour(max_hour)
            if hour < 11:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 10
                total_bill = (base_bill + (15 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break

def package_b(base_bill):
    base_bill = base_bill + 500
    month = get_month()
    if month in month_with_31_days:
        while True:
            max_hour = 744
            hour = get_hour(max_hour)
            if hour < 21:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 20
                total_bill = (base_bill + (10 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break
    elif month in month_with_30_days:
        while True:
            max_hour = 720
            hour = get_hour(max_hour)
            if hour < 21:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 20
                total_bill = (base_bill + (10 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break
    elif month in month_with_28_days:
        while True:
            max_hour = 672
            hour = get_hour(max_hour)
            if hour < 21:
                total_bill = base_bill
                print(f"Bill: ₱{total_bill}.")
                break
            else:
                additional_hours = hour - 20
                total_bill = (base_bill + (10 * additional_hours))
                print(f"Bill: ₱{total_bill}.")
                break

#Future Feature
# def show_bill_breakdown(package): 
#     is_show_bill = input('Do you wish to see your bill breakdown (Y/N): ').upper()
#     if is_show_bill == 'Y':
#         print("---Bill Statement---")
#         if package == 'A':
#             print(f"Currentt Package: {package} - ₱200")
#             print(f"Hours Consumed: {} - ₱{()}")

def package_c(base_bill):
    total_bill = base_bill + 900
    print(f"Bill is {total_bill}")
    exit

package = get_package()
if package == 'A':
    package_a(base_bill)

elif package == 'B':
    package_b(base_bill)
elif package == 'C':
    package_c(base_bill)
else:
    exit
