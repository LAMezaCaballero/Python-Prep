class H7list:
    
    def __init__(self, lis_num) :
      #  for element in lis_num:
      #      if type(element) != int:
      #          self.lista = []
      #          raise ValueError('la lista debe tener solo numeros. se a creado una lista vacia.')
             
        if type(lis_num) != list:
            self.lista = []
            raise ValueError('la lista debe tener solo numeros. se a creado una lista vacia.') 
        else:
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
        resultadosprimos=[]
        for i in self.lista:
            if (self.primo(i)) :
                
                resultadosprimos.append(True)
            else:
                
                resultadosprimos.append(False)
        return resultadosprimos
       
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
        return moda, maximo
   

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
        #if valor_destino != None:
         #   print(f'la temp {valor} {origen} equivale a {valor_destino} {destino}')
        return valor_destino      

    def conver_grados_lista(self, origen, destino):
         #revisar si los grados son bien hechos.
        parametros_esperados = ['celsius', 'farenheit', 'kelvin']
        lista_convertir = []
        if (str(origen) not in parametros_esperados):
            print(f'el dato de origen no esta dentro de los valores esperados {parametros_esperados}')
            return None
        if  not(str(destino) in parametros_esperados):
            print('el dato de destino no esta dentro de los valores esperados', parametros_esperados)
            return None
        resultadosgrados = []
        for i in self.lista:
            resultadosgrados.append(self.conver_grados(i, origen, destino))
        return resultadosgrados
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
        resultadosFactorial = []
        for i in self.lista:
            resultadosFactorial.append(self.factorial(i))
        return resultadosFactorial

