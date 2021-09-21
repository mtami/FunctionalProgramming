from functional import seq


# i add few extra examples for the Closures

def multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = multiplier_of(3)

# Multiplier of 5
times5 = multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

print('-'*10)

# All function objects have a __closure__ attribute
# that returns a tuple of cell objects if it is a closure function
print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)

print('-'*10)


# GrossSalaryCalc example from the session recording
def gross_salary_calculator(base_salary):
    tax = 0.2 * base_salary

    def total(bonus):
        return bonus + tax + base_salary

    return total


employees_basic_salaries = [
    ('a', 1000),
    ('b', 2000),
    ('c', 3000)
]

# using built-in function `map`
gross_salary_calcs = list(map(lambda x: {'id': x[0], 'gross_salary_calculator': gross_salary_calculator(x[1])},
                              employees_basic_salaries))

print(f"Employee {gross_salary_calcs[0]['id']} Salary: ", gross_salary_calcs[0]['gross_salary_calculator'](80))
print(f"Employee {gross_salary_calcs[1]['id']} Salary: ", gross_salary_calcs[1]['gross_salary_calculator'](90))
print(f"Employee {gross_salary_calcs[2]['id']} Salary: ",
      list(filter(lambda x: x['id'] == 'c', gross_salary_calcs))[0]['gross_salary_calculator'](100))

print('-'*10)

# using `functional` external package https://github.com/EntilZha/PyFunctional
gross_salary_calcs2 = (seq(employees_basic_salaries)
                       .select(lambda x: {'id': x[0], 'gross_salary_calculator': gross_salary_calculator(x[1])}))

print(f"Employee {gross_salary_calcs2[0]['id']} Salary: ", gross_salary_calcs2[0]['gross_salary_calculator'](80))
print(f"Employee {gross_salary_calcs2[1]['id']} Salary: ", gross_salary_calcs2[1]['gross_salary_calculator'](90))
print(f"Employee {gross_salary_calcs2[2]['id']} Salary: ", gross_salary_calcs2[2]['gross_salary_calculator'](100))