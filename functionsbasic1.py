# Defines a function called calculate_age and tells it how to calculate someone's age given the years, then asks it to return that value.

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

# Defines my_age and dads_age using an output from the function calculate_age.

my_age = calculate_age(2049, 1993)

dads_age = calculate_age(2049, 1953)

# Prints a statement using the two variables above.

print("I am "+str(my_age)+" years old and my Dad is "+str(dads_age)+" years old.")
