def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    #si el string está vacío, el número es 0
    if not romano:
        return 0

    #si hay un carácter, devolver su valor
    if len(romano) == 1:
        return valores[romano]

    #se suma cuando el primer y el segundo valor es mayor o igual que el segundo 
    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        #cuando el primer valor es menor que el segundo, se resta
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])

# Ejemplo de uso
print(romano_a_decimal('IXX'))   # 19
print(romano_a_decimal('CL'))  # 150