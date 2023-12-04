
def foo(valor):
    if valor:
        print('Valor é verdadeiro')
    else:
        print('Valor é falso')


foo('')
foo(None)
foo(True)
valor = bool()

print(f"Valor {valor}")

valor = bool("Oi")

print(f'Valor {valor}')
