#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class vehiculo:
    def __init__(self, color, tipo, cilindrida):
        self.color = color
        self.tipo = tipo
        self.cilindrida = cilindrida


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class vehiculo:
    def __init__(self, color, tipo, cilindrida):
        self.color = color
        self.tipo = tipo
        self.cilindrida = cilindrida
        self.vel = 0
        self.direccion = 0
#metodos
    def acel(self, vel):
        self.vel += vel
    
    def frena(self, vel):
        self.vel -= vel
    
    def doblar(self, grados):
        self.direccion +=grados




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

a = vehiculo('blanco','camioneta', 6)
s= vehiculo('negro','moto',2)
d= vehiculo('gris','camion','12')



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class vehiculo:
    def __init__(self, color, tipo, cilindrida):
        self.color = color
        self.tipo = tipo
        self.cilindrida = cilindrida
        self.vel = 0
        self.direccion = 0
#metodos
    def acel(self, vel):
        self.vel += vel
    
    def frena(self, vel):
        self.vel -= vel
    
    def doblar(self, grados):
        self.direccion +=grados

    def status(self):
       print( 'la velo', self.vel, 'la dire', self.direccion)

    def detalle(self):
        print(f'color {self.color}  tipo {self.tipo}  cilindrada {self.cilindrida}')





# In[13]:

a = vehiculo('blanco','camioneta', 6)
s= vehiculo('negro','moto',2)
d= vehiculo('gris','camion','12')




# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:


class H7:
    
    def __init__(self) :
        pass

    def primo(self, num):
        loes = True
        for i in range (2, num):
            if  num%i ==0:
                loes = False
                break
        return loes

    def valor_modal(self, lista, menor=True):
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

    def conver_grados(self, valor, origen, destino):
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


    def factorial(self, num):
        if type(num) != int:
            return 'El número debe ser un entero'
        if num < 0:
            return 'El número debe ser positivo'

        if num > 1:
            num = num * self.factorial(num-1)
        return num     




# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

h=H7()
h.factorial(5)
h.primo(16)
listado = [1,8,2,5,4,8,10,7]
moda, repe = h.valor_modal(listado, True)
print(f'la moda es {moda} y se repite {repe}')


# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

class H7list:
    
    def __init__(self, lis_num) :
        self.lista = lis_num
        
#---------------------------primo----------------------------------------
    def primo(self, num):
        loes = True
        for i in range (2, num):
            if  num%i ==0:
                loes = False
                break
        return loes

    def primolista(self):
        for i in self.lista:
            if (self.primo(i)) :
                print(f'el numero {i} Si es primo')
            else:
                print(f'el numero {i} No es primo')
#---------------------------moda----------------------------------------
    def valor_modal_lista(self, menor=True):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if menor:
           self.lista.sort()
        else:
            self.lista.sort(reverse=True)    
        for elemento in self.lista:
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
        return print(f'el valor modal es {moda}, y se repite {maximo} veces')

   

#---------------------------temperatura----------------------------------------
    def conver_grados(self, valor, origen, destino):
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

    def conver_grados_lista(self, origen, destino):
        for i in self.lista:
            self.conver_grados(i, origen, destino)
#---------------------------factorial----------------------------------------
    def factorial(self, num):
        if type(num) != int:
            return 'El número debe ser un entero'
        if num < 0:
            return 'El número debe ser positivo'

        if num > 1:
            num = num * self.factorial(num-1)
        return num     

    def factorial_lista(self):
        for i in self.lista:
            print ('el factorial de ',i,'es', self.factorial(i))




# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

from H7 import H7list

hlist2 = H7list([1,1,1,2,2,2,3,3,3,4,4,4,5,4])
hlist2.conver_grados_lista('farenheit','kelvin')
hlist2.factorial_lista()


# %%
