import math
number = int(input())

result_log = math.log2(math.log2(number))
is_degree = result_log == round(result_log)
print(is_degree)
