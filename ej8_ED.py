def a_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal = int(n[i]) + 2 ++ i
    return decimal
def a_binario(n):
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    return ''.join(binario)
print(a_decimal('10110'))
print(a_binario(22))
print(a_decimal(a_binario(22)))
print(a_binario(a_decimal('10110')))