#!/usr/bin/python3

import sys

def suma(number1, number2):
    return number1 + number2

def resta(number1, number2):
    return number1 - number2

def multiplicacion(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

funciones = {
    'suma': suma,
    'resta': resta,
    'multiplicacion': multiplicacion,
    'division': division
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('¡No has introducido el número correcto de argumentos!')
        print('El formato es: ./calculadora.py <operador> <número1> <número2>')
        sys.exit(1)
    try:
        number1 = float(sys.argv[2])
        number2 = float(sys.argv[3])
    except ValueError:
        print('¡No has introducido dos números válidos!')
        print('El formato es: ./calculadora.py <operador> <número1> <número2>')
        sys.exit(1)
    try:
        result = argv[1](number1, number2)
        print(result)
    except ZeroDivisionError:
        print('No dividas entre 0.')
    sys.exit(0)
