'''
Ejercicio 1.4 Escriba un programa que capture del usuario dos valores a y b 
en dos inputs sucesivos. Pida al usuario desde la función input que los valores 
a ingresar deben contener al menos un número decimal.  Al ejecutar, el programa 
debe realizar la multiplicación entre los dos valores y entregar la respuesta 
en un formatted string que contenga una variable llamada resultado y el texto 
de su preferencia. 

'''

#valores
entrada_1=int(input("ingrese un numero con almenos un decimal: "))
entrada_2=float(input("ingrese otro numero con almenos un decimal: "))

a=entrada_1*entrada_2

print(a)
#operacion
