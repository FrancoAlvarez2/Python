
from funciones import *
        
        


def menu():
    print('|---------------------Menu de opciones------------------------------ |')
    print('1)| Cargar                                                           |')
    print('2)| Mostrar                                                          |')
    print('3)| Mostrar resultados y clase con mayor recaudacion                 |')
    print('4)| Mostrar todos los pasajes vendidos que correspondan a la clase 3 |')
    print('5)| Buscar un pasajero por pasaporte                                 |')
    print('0)| Salir                                                            |')
    print('---------------------------------------------------------------------|')
    return int(input('Ingresar opcion: '))







def main():
    #vector principal
    v_pasaje = []
    opc = -1
    while opc != 0:
        
        opc = menu()
        if opc == 1:
            n = validar_n()
            cargar_arreglo(v_pasaje, n)
        elif opc == 2:
            
            ordenar(v_pasaje)
            mostrar_datos(v_pasaje)
                
        elif opc == 3:
            v_acum = crear_acumuladores_op3(v_pasaje)
            determinar_mayor_op3(v_acum)
        elif opc == 4:
            prom = calcular_promedio(v_pasaje)
            mostrar_datosop4(v_pasaje, prom)
        elif opc == 5:
            pasaporte = input('Ingrese un pasaporte (ABCDE): ')
            pos = busqueda_lineal(v_pasaje, pasaporte)
            if pos >= 0:
                print('Pasajero', v_pasaje[pos].nombre, ', por favor concurrir a atencion al cliente.')
                print(v_pasaje[pos])
            else:
                print('No se encontro un pasaje con ese pasaporte.')
            





if __name__ == '__main__':
    main()