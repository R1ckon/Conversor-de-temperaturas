def celcius_kelvin(unidade1):
    return unidade1 + 273

def kelvin_celcius(unidade1):
    return unidade1 - 273

def fahrenheit_celcius(unidade1):
    return (unidade1 - 32) * 5 / 9

def celcius_fahrenheit(unidade1):
    return (unidade1 * 9 / 5) + 32

def fahrenheit_kelvin(unidade1):
    return (unidade1 - 32) * 5 / 9 + 273.15

def kelvin_fahrenheit(unidade1):
    return (unidade1 - 273.15) * 9 / 5 + 32


unidade1 = float(input('Qual valor deseja converter?'))
operaçao = int(input("""Qual operação deseja fazer?)
                 1.celcius => kelvin
                 2.celcius => fahrenheit
                 3.fahrenheit => celcius
                 4.fahrenheit => Kelvin
                 5.kelvin => celcius
                 6.kelvin => fahrenheit
                 """))

if operaçao == 1:
    resultado = celcius_kelvin(unidade1)
elif operaçao == 2:
    resultado = celcius_fahrenheit(unidade1)
elif operaçao == 3:
    resultado = fahrenheit_celcius(unidade1)
elif operaçao == 4:
    resultado = fahrenheit_kelvin(unidade1)
elif operaçao == 5:
    resultado = kelvin_celcius(unidade1)
elif operaçao == 6:
    resultado = kelvin_fahrenheit(unidade1)
else:
    resultado = "Operação inválida"

print(resultado)