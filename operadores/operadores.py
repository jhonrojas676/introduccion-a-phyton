'''
operadores matematicos
suma
resta
multiplicacion
division
potencia
floor division
modulo


'''
#operador suma
x=2
y=5
print(x+y) #suma
print(type(x), type(y))
w=2.5
z=x+w
print(z, type(z))

#operador resta
a=10
b=15
c=b-a
print("el resultado de la resta es:", c, type(c))

#operador division
d=12
f=4
print(d/f, type(d/f))

#operador multiplicacion
a=50
print(2*a, type(2*a))

#operador potencia
y=a**f
print(f"el numero {a} elevado a la variable f {f} es {y}")

#operador floor division o division piso
m=50
n=3
print(m//n)

#operador modulo
g=10
h=3
print(g%h) #respuesta: 1 -> es el residuo de la division

print(8//-3) #devuelve -3 porque redondea hacia el numero menor
print(8/-3)  #devuelve -2.6666 la diferencia es que no redondea hacia el numero menor

''' operadores de comparacion
este tipo de operadores  los usamos cuando deseamos comparar expresiones
phyton evalua si se cumple la comparacion
y nos devuelve(retorna) un valor True o False


'''
#es igual a
print(2==2) #True
print(2==3) #False  

x=4.123456789000001058946546
y=4.123456789000001
print(x==y) #True porque phyton redondea el numero con un numero limite de decimales

