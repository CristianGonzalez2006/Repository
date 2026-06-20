from dataclasses import dataclass
@dataclass(frozen=True)

class RegistroAtencion:
    sku: str
    carnet: str
    recursos: list
    nombre_empleado: str
    codigo_usuario: str
    
    def __init__(self, sku: str, carnet: str, recursos: list, nombre_empleado: str, codigo_usuario: str):
        self.sku = sku
        self.carnet = carnet
        self.recursos = recursos
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario

        if len(self.recursos) >= 5:
            raise ValueError("Limite de recursos por atencion alcanzados")
        
class Recurso:
    def __init__(self, codigo: str, dias_retraso: int = 0):
        self.codigo = codigo
        self.dias_retraso = dias_retraso

Lista_espera = int(input())
PrestamoLibro = Recurso.dias_retraso * 2.50
UsoSalaEstudio = Recurso.dias_retraso * Lista_espera
        
CalcularMulta = int(input("Ingrese el  recurso, 1: PrestamoLibro, 2: UsoSalaEstudio): "))    
if CalcularMulta == 1:
    print("La multa por el prestamo del libro es:", {PrestamoLibro})    
elif CalcularMulta == 2:
    print("La multa por el uso de la sala de estudio es:", {UsoSalaEstudio})
else:
    print("Opcion no valida")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    