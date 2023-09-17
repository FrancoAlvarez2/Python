import random
from clasecruc import *




#---------------------------------------------------------------------
#opc 1
def validar_n():
    n = int(input('Ingresar cant de pasajes a cargar: '))
    while n <= 0:
        n = int(input('Ingresar cant de pasajes a cargar: '))
    return n




def cargar_arreglo(v_pasaje, n):
    pasap = 'ABCDE'
    for i in range(n):
        pasaporte = random.choice(pasap)
        nombre = random.choice(pasap.lower())
        destino = random.randint(100,103)
        clase = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)
        pasa = Pasaje(pasaporte, nombre, destino, clase, importe)
        v_pasaje.append(pasa)
        
#---------------------------------------------------------------------       
#opc 2
def ordenar(v_pasaje):
    n = len(v_pasaje)
    for i in range(n-1):
        for j in range(i+1,n):
            if v_pasaje[i].importe < v_pasaje[j].importe:
                v_pasaje[i], v_pasaje[j] = v_pasaje[j], v_pasaje[i]
                
                
def mostrar_datos(v_pasaje):
    
    for i in range(len(v_pasaje)):
        
            print(v_pasaje[i])
    
        
#---------------------------------------------------------------------       
#opc3

def crear_acumuladores_op3(v_pasaje):
    v_acum = [0] * 10
    print(v_acum)
    for i in range(len(v_pasaje)):
        v_acum[v_pasaje[i].clase-1] += v_pasaje[i].importe
    return v_acum


def determinar_mayor_op3(v_acum):
    may = 0
    for i in range(len(v_acum)):
        if v_acum[i] > 0:
            print('De la clase', i+1,'el importe acumulado es: ', v_acum[i])
        if v_acum[i] > may:
            may = v_acum[i]
    for i in range(len(v_acum)):
        if v_acum[i] == may:
            print('La clase', i+1, 'es la q tiene el mayor importe acumulado: ', v_acum[i])
            
#---------------------------------------------------------------------           
#opc 4
def calcular_promedio(v_pasaje):
    acum = 0
    cont = 0
    for i in range(len(v_pasaje)):
        if v_pasaje[i].clase == 3:
            acum += v_pasaje[i].importe
            cont += 1
    prom = 0
    if cont > 0:
        prom = acum/cont
    return prom
        
def mostrar_datosop4(v_pasaje, prom):
    for i in range(len(v_pasaje)):
        if v_pasaje[i].clase == 3 and v_pasaje[i].importe > prom:
            print(v_pasaje[i])
            
#---------------------------------------------------------------------           
#opc 5
def busqueda_lineal(v_pasaje, pasaporte):
    for i in range(len(v_pasaje)):
        if v_pasaje[i].pasaporte == pasaporte:
            return i
    return -1