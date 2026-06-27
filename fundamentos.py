""" name = "josefino"
last_name = "guevara"
print(name, last_name) """

#operadores matematicos
number1 = 10
number2 = 20

suma=number1 + number2
resta=number1 - number2
multiplicacion=number1 * number2
division=number1 / number2
"""
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}") """

""" print(number1>number2)
print(number1<number2)
print(number1==number2)
print(number1!=number2)
print(number1>=number2)
print(number1<=number2) """

#condicionales
""" if number1 > number2:
    print(f"el numero {number1} es mayor que {number2}")
else:
    print(f"el numero {number2} es mayor que {number1}") """

#condicionales anidados
puesto="cajero"
edad="25"
""" if puesto=="vendedor":
    print("tiene comision")
    if edad>="18":
        print("puede trabajar")
    else:
        print("no puede trabajar")
else:
    print("no tiene comision") """

#condicionales encadenados
""" if number1 > number2:
    print(f"el numero {number1} es mayor que {number2}")
elif number1 < number2:
    print(f"el numero {number2} es mayor que {number1}")
else:
    print(f"el numero {number1} es igual a {number2}") """

#operadores logicos
""" if (puesto=="vendedor" or puesto=="cajero") and edad>="18":
    print("tiene comision y puede trabajar")
else:
    print("no tiene comision o no puede trabajar") """

#Piedra, papel y tijeras
player1="Pedro"
player2="Juan"
sel_pl1="Papel"
sel_pl2="Tijera"

if sel_pl1=="Piedra" and sel_pl2=="Papel":
    print(f"{player2} gano la ronda")
elif sel_pl1=="Piedra" and sel_pl2=="Tijera":
    print(f"{player1} gano la ronda")
elif sel_pl1=="Tijera" and sel_pl2=="Piedra":
    print(f"{player2} gano la ronda")
elif sel_pl1=="Tijera" and sel_pl2=="Papel":
    print(f"{player1} gano la ronda")
elif sel_pl1=="Papel" and sel_pl2=="Piedra":
    print(f"{player1} gano la ronda")
elif sel_pl1=="Papel" and sel_pl2=="Tijera":
    print(f"{player2} gano la ronda")
else:
    print("Empate")
