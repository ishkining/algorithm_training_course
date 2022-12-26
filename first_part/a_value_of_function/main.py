quadratic_equation_data = [int(number) for number in input().split(' ')]
result = (quadratic_equation_data[0] * quadratic_equation_data[1] ** 2) + \
         (quadratic_equation_data[2] * quadratic_equation_data[1]) + quadratic_equation_data[3]
print(result)