#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def primo(num):
    loes = True
    for i in range (2, num):
        if  num%i ==0:
            loes = False
            break
    return loes    





# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def extraer_primos_de_lista(lista):
    lista_primos=[]
    for elemento in lista:
        if primo(int(elemento)):
            lista_primos.append(elemento)
    return lista_primos

lis_completa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lis_primos = extraer_primos_de_lista(lis_completa)
lis_primos
# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo

l=[1,2,2,2,3,4,5,5,6,7,7,7]

valor_modal(l)

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# In[45]:

def valor_modal(lista, menor=True):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    if menor:
        lista.sort()
    else:
        lista.sort(reverse=True)    
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo
l=[1,2,2,2,3,4,5,5,6,7,7,7]

valor_modal(l,False)
# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def conver_grados(valor, origen, destino):
    valor_destino=None
    if origen == destino:
        print('es el mismo')
        valor_destino = valor
    elif origen == 'celsius':
        if destino == 'farenheit':
            valor_destino = (valor * 9 / 5) + 32  
        elif destino == 'kelvin':
            valor_destino = valor + 273.15
    
    elif origen == 'farenheit':
        if destino == 'celsius':
            valor_destino = (valor  + 32 )/9 * 5 
        elif destino == 'kelvin':
            valor_destino =(valor * 9 / 5) + 32 + 273.15

    elif origen == 'kelvin':
        if destino == 'farenheit':
            valor_destino = ((valor-273.15 )* 9 / 5) + 32  
        elif destino == 'celsius':
            valor_destino = valor - 273.15

    else : 
        print('el origen o destino son invalidos')
    if valor_destino != None:
        print(f'la temp {valor} {origen} equivale a {valor_destino} {destino}')        
        


# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

grados= ['celsius','kelvin', 'farenheit']

for i in grados:
    for j in grados:
        conver_grados(2,i,j) 


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:



def factorial(num):
    if type(num) != int:
        return 'El número debe ser un entero'
    if num < 0:
        return 'El número debe ser positivo'

    if num <= 1:
        return 1
    
    num = num * factorial(num-1)
    
    return num
