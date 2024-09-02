class Banco():
    def __init__(self, rut:str = "77777888-9", nom_comercial:str ="Banco de Talca", direccion:str ="Talca") -> None:
        self.__rut = rut
        self.__nom_comercial = nom_comercial
        self.__direccion = direccion


class Cuenta(Banco):
    def __init__(self, id_cuenta:str, rut: str = "77777888-9", nom_comercial: str = "Banco de Talca", direccion: str = "Talca", saldo:int=0 ) -> None:
        super().__init__(rut, nom_comercial, direccion)
        self.__id_cuenta=id_cuenta
        self.__saldo=saldo
  
    def set_saldo(self, saldo):
        self.__saldo=saldo
    
    def get_saldo(self) -> int:
        return self.__saldo
    
    def get_cuenta(self) -> str:
        return self.__id_cuenta

class Cta_corriente(Cuenta):
    def __init__(self, id_cuenta: str, rut: str = "77777888-9", nom_comercial: str = "Banco de Talca", direccion: str = "Talca", saldo: int = 0, linea_credito:bool=True) -> None:
        super().__init__(id_cuenta, rut, nom_comercial, direccion, saldo)
        super().__init__(rut, nom_comercial, direccion, id_cuenta, saldo)
        self.__linea_credito=linea_credito

    def set_lineacred(self, opcion:bool):
        self.__linea_credito = opcion
    
    def get_lineaCredito(self) ->bool:
        return self.__linea_credito
    
class Cta_ahorro(Cuenta):
    def __init__(self, id_cuenta: str, rut: str = "77777888-9", nom_comercial: str = "Banco de Talca", direccion: str = "Talca", saldo: int = 0, cant_giros:int=0, intereses:bool=True) -> None:
        super().__init__(id_cuenta, rut, nom_comercial, direccion, saldo)
        super().__init__(rut, nom_comercial, direccion, id_cuenta, saldo)
        self.__cant_giros=cant_giros
        self.__intereses=intereses

    def set_giros(self, cant_giros):
        self.__cant_giros = cant_giros
    
    def get_giros(self) -> int:
        return self.__cant_giros
    
    def set_intereses(self, intereses):
        self.__intereses = intereses

    def get_intereses (self) -> bool:
        return self.__intereses

class Cliente(Cta_ahorro,Cta_corriente):
    def __init__(self, id_cliente:str, nom_cliente:str, dir_cliente:str,id_cuenta: str, rut: str = "77777888-9", nom_comercial: str = "Banco de Talca", direccion: str = "Talca", saldo: int = 0, cant_giros: int = 0, intereses: bool = True, contrasena_usuario:str = "123") -> None:
        super().__init__(id_cuenta, rut, nom_comercial, direccion, saldo, cant_giros, intereses)

        self.__id_cliente = id_cliente
        self.__nom_cliente =   nom_cliente
        self.__dir_cliente = dir_cliente
        self.__contrasena_usuario = contrasena_usuario


    def get_id_cliente (self) -> str:
        return self.__id_cliente
    
    def get_nom_cliente (self) -> str:
        return self.__nom_cliente
    
    def get_dir_cliente (self) -> str:
        return self.__dir_cliente
    
    def set_dir_cliente(self, dir_cliente):
        self.__dir_cliente = dir_cliente

    def get_clave(self) -> str:
        return self.__clave
    
    def set_clave(self, clave:str):
        self.__clave=clave

