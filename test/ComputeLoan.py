"""
Step 1. Prompt the user to enter the annual interest rate, number of years, and loan amount.

Step 2. The input for the annual interest rate is a number in percent format, such as 4.5%.
The program needs to convert it into a decimal by dividing it by 100.

To obtain the monthly interest rate from the annual interest rate, divide it by 12, since a year has
12 months. So to obtain the monthly interest rate in decimal format, you need to
divide the annual interest rate in percentage by 1200. For example, if the annual
interest rate is 4.5%, then the monthly interest rate is

monthly_interest_rate = annual_interest_rate / 1200


Step 3. Compute the monthly payment using the formula given in Stage 2.

Step 4. Compute the total payment, which is the monthly payment multiplied by 12and
multiplied by the number of years.

Step 5. Display the monthly payment and total payment.
"""

# prompt User
annual_interest_rate = eval(input("Enter the Annual Interest Rate: "))
number_of_years = eval(input("Enter the Number of Years: "))
loan_amount = eval(input("Enter the Loan Amount: "))

# doublecheck
print("Check the above entered information for correctness:")
print("1. The Annual Interest Rate is: ", annual_interest_rate, "%")
print("2. The Number of Years: ", number_of_years)
print("3. THe Loan Amount: ", loan_amount)
print("===============================================================")

user_answer: str = input("Type 'yes' if everything is correct/ 'no' if sth is wrong: ")
if user_answer.lower() == "no":
    print("❌ OK! let's re-check the information again!")
    exit(1)
else:
    print("✅ Alright, let's continue")

print("===============================================================")
monthly_interest_rate = annual_interest_rate / 1200
print("Let's calculate the Monthly Interest Rate first: ", monthly_interest_rate)

print("===============================================================")
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 / (1 + monthly_interest_rate) ** (number_of_years * 12)))
print("Now let's calculate the Monthly Payment: ", monthly_payment)

print("===============================================================")
total_payment = monthly_payment * number_of_years * 12
print("Now we calculate the Total Payment: ", total_payment)

print("===============================================================")
print("Finally, let's display:")
print("1. Monthly Payment: ", monthly_payment)
print("2. Total Payment: ", total_payment)