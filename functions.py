'''
      Functions
(1) Define vs Call 
(2) Parametr vs Argument
(3) Keywords & default argumnets 
(4) Scope (local vs global)
'''
#  ---- Define vs Call ---

# Define a function


def greet():
    print("Hello, developer!")


# Call the function
greet()
greet()

#  ---- Parametr vs Argument ----

# name and age are parameters


def introduce(name, age):
    print(f"My name is {name}, and I am {age} years old.")


# "Alex" and 24 are arguments
introduce("Alex", 24)


#     ---  Keywords & default argumnets  ---

def calculate_salary(salary, bonus):
    total = salary + bonus
    print(f"Total salary: {total}")


# Pass arguments by parameter name
calculate_salary(salary=3500000, bonus=500000)

#    ---  Scope local  ---


def calculate_total():
    price = 100
    tax = 10
    total = price + tax

    print(total)


calculate_total()

# price is not available outside the function
# print(price)  # NameError

#    ---  Scope global  ---
count = 10


def show_count():
    count = 5
    print("Local count:", count)


show_count()
print("Global count:", count)
