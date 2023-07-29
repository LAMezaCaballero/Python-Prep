#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

lis= ['mty', 'san nico', 'escomiedo','sparta','so']
print(lis)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(lis[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(lis[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:


print(type(lis))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:



print(lis[2:])

# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(lis[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

lis.append('Ciudad de Méjico')
lis.append('mty')







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

lis.insert(3,'gdl')



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

lis.extend(['lol','aov'])
print(list)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(lis.index('mty'), lis.index('Ciudad de Méjico'))



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:


#marca error is not in list


# 12) Eliminar un elemento de la lista

# In[25]:


lis.remove('mty')



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

# error list.remove(x) x no existe


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:


ulti = lis.pop()
print(ulti)


# 15) Mostrar la lista multiplicada por 4

# In[29]:


print(lis*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
num_tuple= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(num_tuple[9:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in num_tuple)
print(30 in num_tuple)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:


elem= 'París'
if not(elem in lis):
    lis.append(elem)
    print(f'{elem} se agrego a lista')
else:
    print(f'{elem} ya existia en lista')


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:


print(num_tuple.count(10))
print(lis.count('Ciudad de Méjico'))



# 21) Convertir la tupla en una lista

# In[52]:


type(list(num_tuple))


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


a1,a2,a3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_=num_tuple
print(a1,a2,a3)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


dicc={'cd': lis,
'pais': ['bra','usa','mex', 'uru', 'cle','ven'],
'Cont': ['ame', 'eu', 'afr', 'afr' ]}



# 24) Imprimir las claves del diccionario

# In[59]:

print(dicc.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(dicc['cd'])


