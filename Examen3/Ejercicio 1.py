class Sucursal:
    cuentas={}
    def __init__(self,direccion,provincia,ID):
        self.direccion=direccion
        self.provincia=provincia
        self.ID=ID
    def anidirCuenta(self,cuenta):
        self.cuentas[cuenta.ID]=cuenta

class Cuenta:
    def __init__(self,ID,saldo,titular,sucursal):
        self.ID=ID.zfill(12)
        self.ID=f"ES68 {sucursal.ID} {ID}"
        self.saldo=saldo
        self.titular=titular
        self.sucursal=sucursal

class Cliente:
    def __init__(self,nombre,apellidos,nif,telefono,sucursal,cuenta):
        self.nombre=nombre
        self.apellidos=apellidos
        self.nif=nif
        self.telefono=telefono
        self.sucursal=sucursal
        self.cuenta=cuenta



def mostrarCuentas(cliente):
    print(f"{cliente.nombre}. Cliente de la sucursal {cliente.cuenta.sucursal.ID} ({cliente.cuenta.sucursal.provincia})")
    print(f"{cliente.cuenta.ID} - Saldo: {cliente.cuenta.saldo} $")

def mostrarIbanSucursal(sucursal):
    print(f"Cuentas de la sucursal {sucursal.ID} ({sucursal.provincia})")


sucursal1=Sucursal("Calle Plaza Mayor, 1","Madrid","0055")
sucursal2=Sucursal("Calle Plaza Menor, 2","Sevilla","1234")
sucursal3=Sucursal("Calle Plaza Mediana,3","Barcelona","4444")

cuenta1=Cuenta("123456789012",254,"Mohamed Bada",sucursal1)
cuenta2=Cuenta("012648925",6987,"José Maria",sucursal2)
cuenta3=Cuenta("012648925",6987,"José Maria",sucursal3)

cliente1=Cliente("Mohamed","Bada Sellami","143669827F","65498759",sucursal1,cuenta1)
cliente2=Cliente("Jose","Maria","143669827F","65498759",sucursal2,cuenta2)

mostrarCuentas(cliente1)
mostrarCuentas(cliente2)
mostrarIbanSucursal(sucursal1)