import sys
if len(sys.argv) == 2:# al llamar solo se pedira si llovio
    import datetime
    import os #para poder llamar a otros archivos txt csp py
    marca_de_tiempo= datetime.datetime.now() 
    marca_de_tiempo= int(datetime.datetime.timestamp(marca_de_tiempo))

    lluvia= sys.argv[1]
    temperatura= input('ingrese la temp en grados celsius')
    humedad = input('ingrese humedad')
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad+ ',' + lluvia

    logs_lluvia= open('clase09_ej2.csv', 'a')
    logs_lluvia.write(linea+ '\n')
    logs_lluvia.close

else:
    print('error: introdujo una cantidad de argumentos distito a tres')
    print( 'ejemplo clase09_ej2.py temperatura humedad falso')