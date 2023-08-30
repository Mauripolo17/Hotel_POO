class guest:
    
    def __init__(self, name, cc, tg):
        self.name=name
        self.cc=cc
        self.tg=tg


    def str(self):
        return print(f"Nombre: {self.name} CC {self.cc} tipo {self.tg}")
    
    def Benefits(self):
        pass

class premium_guest(guest):
    def __init__(self, name, cc):
        super().__init__(name, cc, "VIP")
    
    def Benefits(self):
        print("-20% de descuento si se queda mas de 3 dias \n-Desayuno a la habitacion \n-Postre gratis en el restaurante \n-Botella gratis Blue Label en el bar de 750ml")

        

class simple_guest(guest):
    def __init__(self, name, cc):
        super().__init__(name, cc, "VIP")
    
    def Benefits(self):
        print("-5% de descuento si se queda mas de 3 dia ")

class double_guest(guest):
    def __init__(self, name, cc):
        super().__init__(name, cc, "Doble")
    
    def Benefits(self):
        print("-10% de descuento si se queda mas de 3 dias \n-Desayuno gratis")


