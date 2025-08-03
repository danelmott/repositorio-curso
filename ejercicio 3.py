# cajero automatico

class CuentaBancaria:
    def __init__(self,nombre,saldo,pin):
        self.nombre = nombre
        self.saldo = saldo
        self.pin = pin


def CajeroAutomatico(pin):
    if pin != cuentaDanel.pin:
       print("pin incorrecto intentalo de nuevo...")
    elif pin == cuentaDanel.pin:

     while True:
      print("---Cajero Automatico---")
      print("---1:ver saldo---")
      print("---2:retirar saldo---")
      print("---3:hacer deposito---")
      print("---4:salir ---")
      eleccion = int(input("que deseas realizar:"))

    #condicionales para ver saldo
      if eleccion == 1:
        print(f"tu saldo es:{cuentaDanel.saldo}")
     
    # condicionales para retiro
      elif eleccion == 2:
          retiro = float(input("cuanto deseas retirar:"))
          if retiro > cuentaDanel.saldo:
            print("no tienes suficiente saldo")
          else: 
            cuentaDanel.saldo -= retiro
            print(f"tu retiro de {retiro} exitoso tu nuevo saldo es {cuentaDanel.saldo}")
        
    # condicionales para deposito
      elif eleccion == 3:
         desposito = float(input("cuanto deseas depositar:"))
         cuentaDanel.saldo += desposito
         print(f"tu deposito fu exitoso nuevo saldo: {cuentaDanel.saldo}")
        
    #condicionales para salir del cajero
      elif eleccion == 4:
         print("gracias por usar nuestro cajero esperemos vuelva pronto")
         break

# cuenta bancaria de prueba
cuentaDanel = CuentaBancaria("danel mantilla",10000,2009)

#testing
CajeroAutomatico(2009)

        


