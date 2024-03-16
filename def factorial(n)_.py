def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorials_list(n):
    factorials = []
    for i in range(n, 0, -1):
        factorials.append(factorial(i))
    return factorials

# Пример использования
n = 6 
print(factorial(n))  # 6
print(factorials_list(n))  # [720, 120, 24, 6, 2, 1]
