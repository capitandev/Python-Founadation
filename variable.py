# 1. int: number (Integer)
age = 25
year = 2026

# 2. float: number(Float)
height = 175.5
price = 19.99

# 3. str: text (String)
name = "Alex"
country = "Uzbekistan"

# 4. bool: true or false (Boolean)
is_student = True
is_married = False

# 변수 출력
print(age)
print(height)
print(name)
print(is_student)
print("Its working clearly ---------------------------------------------------->")
print("Its working clearly ---------------------------------------------------->")
# --------------------------------------------------------------------------------------------
#                                                           Test

#   Developer monthly financial status


# Developer information
developer_name = "Alex"
monthly_salary = 3500000

# Monthly expenses (KRW)
monthly_rent = 700000
food_expenses = 450000
transportation_cost = 100000
other_expenses = 300000

# Calculate total expenses and savings
total_expenses = (
    monthly_rent
    + food_expenses
    + transportation_cost
    + other_expenses
)

monthly_savings = monthly_salary - total_expenses
yearly_savings = monthly_savings * 12

# Evaluate financial status
is_good_salary = monthly_salary >= 3000000
can_save_money = monthly_savings > 0

# Display results
print("Developer:", developer_name)
print("Monthly salary:", monthly_salary)
print("Total expenses:", total_expenses)
print("Monthly savings:", monthly_savings)
print("Yearly savings:", yearly_savings)
print("Is the salary at least 3 million won?", is_good_salary)
print("Can the developer save money?", can_save_money)

# Personal information test with all variable

# Personal information
name = "Alex"
age = 24
height = 1.78
weight = 72.5

# Financial information (KRW)
monthly_income = 3500000
monthly_expenses = 1800000

is_employed = True
is_student = False

# Calculate financial metrics
savings = monthly_income - monthly_expenses
yearly_income = monthly_income * 12

# Calculate BMI
bmi = weight / (height ** 2)

# Evaluate conditions
is_adult = age >= 18
has_savings = savings > 0
is_financially_stable = is_employed and has_savings
can_apply_for_loan = is_adult and is_employed and has_savings

# Display results
print("Name:", name)
print("Age:", age)
print("BMI:", round(bmi, 2))
print("Monthly savings:", savings)
print("Yearly income:", yearly_income)
print("Financially stable:", is_financially_stable)
print("Can apply for a loan:", can_apply_for_loan)
