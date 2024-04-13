# ====================================== DAY 2 PYTHON ======================================

# -----SUM OF TWO DIGITS-----
two_digits_number = input("Write a number with two digts ")
firstN = int(two_digits_number[0])
secondN = int(two_digits_number[1])
result = firstN + secondN
print(result)


# -----BMI CALCULATOR-----
height = float(input("Write your height "))
weight = int(input("Write your weight "))
bmi_result = weight/height**2
print(round(bmi_result, 2))  # rounded to two decimals
print(int(bmi_result))  # printed the result as a whole number
# Division was made directly to a integer using the // operator
print(weight // height ** 2)
print(f"your BMI reuslt is {round(bmi_result, 2)}")


# ------HOW MANY WEEKS LEFT --------
age = int(input("Write your age: "))
total_years = 90
years_left = total_years - age
weeks_left = years_left * 52
days_left = years_left * 365
months_left = years_left * 12
print(
    f"\nBased on an entire life as a 90 years person: \nYou have {days_left} days, {weeks_left} weeks, {months_left} months and {years_left} years left")


# -------TIP CALCULATOR-------
print("Welcome to tip calculator!\n")
bill = float(input("What was the total bill? "))
tip_percentage = int(
    input("What is the tip percentage you would like to pay?"))
tip_value = (tip_percentage / 100) * bill
total_bill = bill + tip_value
people = int(input("In how many people you would like to split the bill?"))
if people == 1:
    print(f"There is no split, the final value is ${round(total_bill, 2)}")
else:
    final_bill = total_bill / people
    print(f"Each person should give ${round(final_bill, 2)}")
