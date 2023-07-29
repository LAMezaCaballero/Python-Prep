#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

b = 10
if (b < 0):
    print('La variable ',b ,' es menor a cero')
elif (b > 0): 
    print('La variable ',b ,' es mayor a cero')
else:
    print('La variable ',b ,' es igual a cero')



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 3.2
b = 2
if type(a) == type(b):
    print(f'Las variables {a} y {b} son del mismo tipo de dato')
else:
    a = 3.2
b = 2
print(f'Las variables {a} y {b} son del diferentes tipo de dato')




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if i % 2 == 0:
        print('El número ', str(i), ' es par')
    else:
        print('El número ', str(i), ' es impar')



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0, 6):
    print('Valor:', str(i), ' Elevado a la cubo:', str(i**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

n = 4
for i in range(0, n):
    pass
print(i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

n = 3
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n > 2):
            n = n - 1
            factorial = factorial * n
        print(f'El factorial es {factorial}')
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')
    



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

n = 1
while n < 10:
    
    for i in range(1, 6): 
        print('la hora es ' +str(n)+':'+ str(i))
    n += 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range(1, 6):
    n = 1
    while n < 3:
        print('la hora es ' +str(i)+':'+ str(n))
        n += 1



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

tope_rango=30
ciclos_con_break = 0
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
    n +=1

n=0    

while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


# In[57]:




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:

tope_rango=100


ciclos_sin_break = 0
n = 0
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
    n +=1

ciclos_con_break = 0

n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')



# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')



# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input('introduce 1 si quieres continuar o solo enter para detener') != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1


# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


n = 100
while(n<=300):
    if (n % 6 == 0 and n%3 ==0 ):
        print('El número es: ', str(n))
        break
    n += 1

# %%
