from modulos.M04S03_Final_m import Cliente
import os
from time import sleep

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def retirar(client:Cliente, monto:int) -> str:
    saldo:int = client.get_saldo()
    if (saldo < monto) or (monto <= 0):
        print(f"El monto ingresado ({monto}) es incorrecto")
        sleep(3)
        return "Hola"
    else:
        saldo=saldo-monto
        client.set_saldo(saldo)
        client.set_saldo(saldo)
        print (f"Retiro realizado, su nuevo saldo es {saldo}")
        sleep(3)
        return "chao"
    
def depositar(client:Cliente, monto:int) -> str:
    '''
    Esta funcion toma el saldo del cliente, y lo actualiza en base del monto
    que se le esta enviando, verifica de todas maneras que el monto ingresado
    no sea un numero negativo o cero

    Parameters
    client(Cliente): Objeto de tipo cliente con la informacion completa de la cuenta
    monto(int): monto correspondiente al deposito a realizar

    Return: Devuelve un booleano que sirve para seguir pidiendo monto a depositar en caso
    de error, o avanzar en el proceso de la aplicacion principal
    
    '''


    saldo = client.get_saldo()
    if (monto <=0):
        return f"monto invalido, intente nuevamente"

    else:
        saldo = saldo+monto
        client.set_saldo(saldo)
        return f"Deposito realizado, su nuevo saldo es de ${saldo}"
    
def ver_saldo(client:Cliente):
    print(f"Su saldo actual es de ${client.get_saldo()}")
    sleep(3)

def menu_depositar(client:Cliente):
    monto= int(0)
    monto=int(input("Ingrese el monto a depositar: "))
    depositar(client,monto)

def menu_girar(client:Cliente):
    limpiar_pantalla()
    monto=int(0)
    monto=int(input("Ingrese el monto a retirar: "))
    retirar(client,monto)