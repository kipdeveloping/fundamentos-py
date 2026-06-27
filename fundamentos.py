""" name = "josefino"
last_name = "guevara"
print(name, last_name) """

#operadores matematicos
print("")
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

""" if sel_pl1=="Piedra" and sel_pl2=="Papel":
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
    print("Empate") """


name_list=["jose", "pablo", "pedro", "juan"]
age_list=[25, 18, 45, 30]

name_list.append("maria")
age_list.append(30)
""" print(f"nombre: {name_list[0]}, edad: {age_list[0]}")
print(f"nombre: {name_list[1]}, edad: {age_list[1]}")
print(f"nombre: {name_list[2]}, edad: {age_list[2]}")
print(f"nombre: {name_list[3]}, edad: {age_list[3]}")
print(f"nombre: {name_list[4]}, edad: {age_list[4]}") """

#mostrar un slice de la lista
""" print(name_list[1:3])
print(age_list[1:3])

#el ultimo elemento de la lista
print(name_list[-1])
print(age_list[-1])
"""
#cambiar el valor del primer elmento de la lista
name_list[0]="josefina"
age_list[0]=26
""" print(name_list)
print(age_list) """

#tupla: conjunto de valores que no se puede modificar
name_tuple=('jose', 'pablo', 'pedro', 'juan')
age_tuple=(25, 18, 45, 30)

#diccionario
name_dict = {
    'name': 'jose', 
    'last_name': 'guevara', 
    'age': 25,
    'weight':70.5,
    'favorite_foods': ["pizza", "hamburguesa", "pasta"],
    'address': {
        'street':"Calle 123",
        'city':"Lima",
        'country':"Peru"
    }
}

""" print(name_dict["address"]["city"])
print(name_dict["favorite_foods"][1]) """

# bucles

""" for name in name_list:
    print(name) """

for var in range(len(name_list)):
    print(f"Hola {name_list[var]}")

print("")