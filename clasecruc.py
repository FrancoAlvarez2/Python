class Pasaje():
    def __init__(self, pasaporte, nombre, destino, clase, importe) -> None:
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.destino = destino
        self.clase = clase
        self.importe = importe
        
        
    def __str__(self) -> str:
        
        
        destino_str = destino_tp_str(self.destino)
        
        
        cadena = 'Pasaporte:  ' + self.pasaporte
        cadena += ' |Nombre: ' + self.nombre
        cadena += ' |destino: ' + destino_str
        cadena += ' |clase: ' + str(self.clase)
        cadena += ' |importe: ' + str(self.importe)
        return cadena
    
    
    
    
    
def destino_tp_str(destino):
    
    #           100         101         102             103
    #ind        0           1           2               3
    paises = ['Bahamas', 'Bermudas', 'Puerto Rico', 'RepublicaDominicana']
    dest = paises[destino-100]
    return dest