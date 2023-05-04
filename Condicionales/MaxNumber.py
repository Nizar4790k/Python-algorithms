"""
4.Dado 3 números Calcular el Mayor (Propuesto)
"""

number1 = float(input("Ingrese el numero1"))
number2 = float(input("Ingrese el numero2"))
number3 = float(input("Ingrese el numero3"))


if number1 == number2 and number2 == number3:
    print(str(number1))
elif number1 > number2 and number1 > number3:
    print(str(number1))
elif number2 > number1 and number2 > number3:
    print(str(number2))
elif number3 > number1 and number3 > number2:
    print(str(number3))

