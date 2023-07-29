#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:

import H7_9 as h

hl= h.H7list([1,2,3,4,5,6,6])
# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:


hl.conver_grados_lista('celsius','kElvin')

hl.conver_grados_lista('cellsius','kelvin')
hl= h.H7list(1)
hl.conver_grados_lista('cellsius','kelvin')

# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:

import unittest
import H7_9 as h
class ProbandoMiClase(unittest.TestCase):
    
    def test_crearobjetoerror(self):
        param = 'hola'
        self.assertRaises(ValueError, h.H7list, param)
    
    def test_crearobjetoCorrecto(self):
        param = [1,2,3,4,5,2]
        h1= h.H7list(param)
        self.assertEqual(h1.lista,param)

    def test_modal(self):
        h1= h.H7list([1,2,3,4,5,2])
        moda, veces = h1.valor_modal_lista() # obtener la moda y las repeticiones del valor modal
               
        self.assertEqual([moda, veces], [2,2]) #comparo [moda,veces] con [2,2]
      
unittest.main(argv=[''], verbosity=2, exit=False)
# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:

import unittest
import H7_9 as h
class ProbandoMiClase(unittest.TestCase):
    
    def test_crearobjetoerror(self):
        param = 'hola'
        self.assertRaises(ValueError, h.H7list, param)

unittest.main(argv=[''], verbosity=2, exit=False)
# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:
importlib.reload(h)
h1= h.H7list([1,2,4])
h1.primolista()

import unittest
class ProbandoMiClase(unittest.TestCase):

    def test_primoFail(self):
        h1= h.H7list([1,2,4])
        results = h1.primolista()
        self.assertEqual(results,[True,False,False]) #debe ser fail.

    def test_primoCorrect(self):
        h1= h.H7list([1,2,4])
        results = h1.primolista()
        self.assertEqual(results,[True,True,False])   


unittest.main(argv=[''], verbosity=2, exit=False) 

# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:
import unittest
import importlib
import H7_9 as h
importlib.reload(h)

h1= h.H7list([1,2,4])

h1.conver_grados_lista('kelvin','celsius')

class Probando_temperatura(unittest.TestCase):
    
    def test_probarcambiodetempcorrect(self):
        h1= h.H7list([1,2,4])
        self.assertEqual(h1.conver_grados_lista('kelvin','celsius'),[-272.15, -271.15, -269.15])

    def test_probarcambiodetempfail(self):
        h1= h.H7list([1,2,4])
        self.assertEqual(h1.conver_grados_lista('kelvin','farenheit'),[-272.15, -271.15, -269.15])

unittest.main(argv=[''], verbosity=2, exit=False)


# 8) Agregar casos de pruebas para el método factorial()

# In[20]:

import unittest
import importlib

import H7_9 as h
importlib.reload(h)


h1 = h.H7list([1,2,3,4,6,7])
#h1.factorial_lista()
resultado = h1.factorial_lista()
print (resultado)

import unittest
#class PruebaClaseFactorial(unittest.TestCase):
class ProbandoMiClase(unittest.TestCase):

    def test_Factoriallista_exito(self):
        h1 = h.H7list([1,2,3,4,6,7])
        resultado = h1.factorial_lista()
        self.assertEqual(resultado,[1, 2, 6, 24, 720, 5040])

    def test_Factoriallista_fail(self):
        h1 = h.H7list([1,2,3,4,6,7])
        resultado = h1.factorial_lista()
        self.assertEqual(resultado,[2, 2, 6, 24, 720, 5040])
        
unittest.main(argv=[''],verbosity=2, exit=False)
 

# %%
