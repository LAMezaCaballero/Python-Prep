import sys

if len(sys.argv) == 4:
    print("el parametro 1 es", sys.argv[1])
    print('el parametro 2 es', sys.argv[2])
    print(f'el parametro 3 es {sys.argv[3]}')
else:
    print('no son 3 parametros.')