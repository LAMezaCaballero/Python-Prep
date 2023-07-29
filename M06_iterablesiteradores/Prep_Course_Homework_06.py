#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

l =[]
n = -15
while n < 0:
    l.append(n) 
    n +=1
print(l)



# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

n = 0
while n < len(l):
    if l[n]%2==0:
        print(l[n])
    n +=1



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for elem in l:  
    if elem % 2 == 0:
        print(elem)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

for e in l[:3]:
    print(e)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for indice, elemento in enumerate(l):
    print(indice,elemento)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

l = [1,2,5,7,8,10,13,14,15,17,20]

n = 1 

while n <= 20: 
    if not (n in l): 
        l.insert(n-1, n)  
    n += 1 

print(l)  



# In[11]:




# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

f= [0,1]
n=2
while n < 30:
    f.append(f[n-1]+f[n-2])
    n+=1
print (f)



# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

sum(f)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

n= len(f)-5
while n < len(f):
    print(f[n] / f[n - 1],' = ', f[n],'/', f[n-1])
    
    n += 1  


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i, c in enumerate(cadena): 
    if c == 'n':  
        print(i) 



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:


dic = {
    'cosa': [1,2,3,4,5,],
    'num': [1,2,3,4,5,],
    'rum':[1,2,3,4,5,]
}

for i in dic:
    print (i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print(type(cadena))  

cadena = list(cadena)
print(type(cadena))

recorre = iter(cadena)
for i in range(len(cadena)):
    print(next(recorre))




# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lis1 = ['tortuga', 'pajaro', 'perro']
lis2 = ['caparazon', 'pluma', 'pelo']
lisz = zip(lis1, lis2)  
print(type(lisz))  
print(list(lisz))



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

l = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]  # Definición de la lista original

l2 = [i for i in l if i % 7 == 0] 
print (l2)



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

print(len(lis), type(lis))

cont= 0
for e in lis:
    if type(e)==list:
        cont += len(e)
    else:
        cont +=1
print(cont)



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

for indice, elemento in enumerate(lis):  # Iteración sobre cada elemento de la lista 'lis' junto con su índice
    if type(elemento) != list:  # Verificación si el elemento no es una lista
        lis[indice] = [elemento] 

print(lis)

