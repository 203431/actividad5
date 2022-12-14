from threading import Thread
from time import sleep

class Mesero(Thread):
    def __init__(self, conditionM, cocinero, order):
        Thread.__init__(self)
        self.conditionM = conditionM
        self.cocinero = cocinero
        self.comida = False
        self.order = order
        
    def attend(self, client):
        self.conditionM.acquire()
        print(f"El mesero está tomando la orden del cliente {client}")
        self.order = [client, False]
        self.sendOrderToCook(client)
        sleep(10)
        self.conditionM.notify()
        self.conditionM.release()
        return self.order
            
    def sendOrderToCook(self, client):
          self.conditionM.acquire()
          print(f"El mesero está llevando la orden de {client} al concinero")
          sleep(5)
          self.cocinero.cocinar(client)
          sleep(2)
          self.conditionM.notify()
          self.conditionM.release()
          print("El mesero está descansando")
          
    def llevarComida(self, client):
        self.conditionM.acquire()
        sleep(5)
        self.conditionM.notify()
        self.conditionM.release()
        self.order = ["", False]
        print("El mesero está descansando")
        return True