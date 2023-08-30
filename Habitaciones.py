
class Rooms:

    def __init__(self, id, typeroom, price, available=True):
        self.id=id
        self.typeroom=typeroom
        self.price=price
        self.available=available
        self.resident=None
    
    def inf(self):
        pass

    def reserve(self):
        self.available=False

    def cost(self, nights):
        pass
    
    def guest(self, resident):
        self.resident=resident
        
    def Benefits(self):
        print("Aqui van los beneficios")

class vip(Rooms):
    
    def __init__(self, id, available=True):
        super().__init__(id, "VIP", 120000, available)
        
    def inf(self):
        print("-Espaciosa \n-Cama King size \n-Aire acondicionado \n-TV 62 pulagada \n-Desayuno a la habitacion \nJacuzzi")

    def Benefits(self):
        return print("-20% de descuento si se queda mas de 3 dias \n-Desayuno a la habitacion \n-Postre gratis en el restaurante \n-Botella gratis Blue Label en el bar de 750ml")
    
    def cost(self, nights):
        if nights > 3:
            return (self.price*nights)*0.8 
        else:
            return self.price*nights


class simple(Rooms):
    
    def __init__(self, id, available=True):
        super().__init__(id, "Sencilla", 50000, available)
        
    def inf(self):
        print("-Espacio 4X3 \n-Cama de un cuerpo \n-Ventilador \n-TV 32 pulgadas")

    def Benefits(self):
        print("-5% de descuento si se queda mas de 3 dia ")
    
    def cost(self, nights):
        if nights > 3:
            return (self.price*nights)*0.95 
        else:
            return self.price*nights


class double(Rooms):
    
    def __init__(self, id, available=True):
        super().__init__(id, "Doble", 80000, available)
        
    def inf(self):
        print("-Espaciosa \n-Cama de dos cuerpos \n-Ventilador \n-TV 52 pulgadas")

    def Benefits(self):
        print("-10% de descuento si se queda mas de 3 dias \n-Desayuno gratis")

    def cost(self, nights):
        if nights > 3:
            return (self.price*nights)*0.9 
        else:
            return self.price*nights
    
