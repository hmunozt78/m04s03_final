from modulos.M04S03_Final_m import Cliente
from modulos.M04S03_Final_f import menu_depositar, ver_saldo, menu_girar, limpiar_pantalla

cliente1 = Cliente("13433689-7", "Hugo Muñoz", "Av. Siemprevida 123", "A-001", saldo = 3000)
cliente2 = Cliente("13433689-7", "Hugo Muñoz", "Av. Siemprevida 123", "B-001", saldo= 2000)
cliente3 = Cliente("1-9", "Kevin Muñoz", "Av. Siemprevida 123", "A-002", saldo=1500)

v_cambiar_cliente=bool(True)

while v_cambiar_cliente:

    limpiar_pantalla()

    v_seleccion_cliente:int

    print(''' 
    Selecciona el Cliente con quien trabajaras:
        1) Hugo Muñoz - Cuenta Corriente
        2) Hugo Muñoz - Cuenta Ahorro
        3) Kevin Muñoz - Cuenta Corriente
        4) Salir
    ''')
    v_seleccion_cliente = int(input("Ingrese la opcion: "))

    if v_seleccion_cliente == 1:
        v_cliente_seleccionado = cliente1
    elif v_seleccion_cliente == 2:
        v_cliente_seleccionado = cliente2
    elif v_seleccion_cliente ==3:
        v_cliente_seleccionado = cliente3
    elif v_seleccion_cliente ==4:
        break


    v_cont_menu_principal= bool(True)


    while v_cont_menu_principal:
        limpiar_pantalla()
        v_opcion_menu_principal:int =0
        print(f'''
        Bienvenido al Banco de Talca
        Todo pasa en Talca
        Nombre Cliente: {v_cliente_seleccionado.get_nom_cliente()} - {v_cliente_seleccionado.get_cuenta()}
            
        1) Realizar Deposito
        2) Realizar Giro
        3) Consultar Saldo
        4) Transferencia - en Desarrollo
        5) Cambiar Cliente
        6) Salir
            
            ''')
        v_opcion_menu_principal = int(input("Ingrese la opcion de su preferencia: "))

        if v_opcion_menu_principal==1:
            menu_depositar(v_cliente_seleccionado)
        elif v_opcion_menu_principal==2:
            menu_girar(v_cliente_seleccionado)
        elif v_opcion_menu_principal==3:
            ver_saldo(v_cliente_seleccionado)
        elif v_opcion_menu_principal == 4:
            print("En Desarrollo")
        elif v_opcion_menu_principal==5:
            v_cont_menu_principal=False
        elif v_opcion_menu_principal==6:
            break
        