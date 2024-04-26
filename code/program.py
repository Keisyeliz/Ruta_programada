list_programacion = []
list_rutas = []
import os 



def fnt_limpiar():
    os.system('cls')
    print('Nombre del preograma: Gestión de rutas')
    print('Autor: Keisy Murillo')
    print('Año: 2024-1')



def fnt_agregar_ruta():
    fnt_limpiar()
    print('---AGREGAR RUTA---')
    code = input('Codigo: ')
    nombre = input('Nombre: ')
    descripcion = input('Descripción: ')
    r = code +' ' + nombre + ' ' + descripcion
    list_rutas.append(r)
    print('\nRuta registrada con exito')
    input('Presione <ENTER> para continuar...')
sw2 = True
def fnt_menu_rutas():
    global sw2
    while sw2 == True:
        fnt_limpiar()
        opcion_r = input('\n---MENÚ RUTAS---\n1. Agregar\n2. Consultar\n3. Salir\n-> ')
        if opcion_r == '1':
            fnt_agregar_ruta()
        if opcion_r == '3':
            sw2 = False

global sw
sw = True

while sw == True:
    fnt_limpiar()
    opcionStr = input('\n---MENÚ PRINCIPAL---\n1. Rutas\n2. Envios\n3. Salir\n-> ')
    if opcionStr == '1':
        fnt_menu_rutas()