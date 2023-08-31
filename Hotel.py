from Habitaciones import *
from Huesped import *

vip1=vip(None, True)
simple1=simple(None, True)
double1=double(None, True)
class Node:
    def __init__(self, room):
        self.room=room
        self.left=None
        self.right=None
    
<<<<<<< HEAD
class TreeHotel:
    def __init__(self):
        self.root=None
=======

class TreeHotel:
    def __init__(self):
        self.root=None
   
    def get_root(self):
        return self.root
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03
    
    def add(self, newRoom):
        if self.root is None:
            self.root=Node(newRoom)
        else:
            self.add_recursive(self.root, newRoom)

    def add_recursive(self, r, newRoom):
        if newRoom.id<r.room.id:
            if r.left is None:
                r.left=Node(newRoom)
            else:
                self.add_recursive(r.left, newRoom)
        else:
            if r.right is None:
                r.right=Node(newRoom)
            else:
                self.add_recursive(r.right, newRoom)
    
    def search(self, r, id):
        if r.romm.id == id:
            return r
        elif id < r.romm.id and r.izq is not None:
            return self.buscar(id, r.izq)
        elif id > r.room.id and r.der is not None:
            return self.buscar(id, r.der)
        else:
            return None
        
<<<<<<< HEAD
    def search_available(self, node, typeh, name1, cc):
        if node is not None:
            self.search_available(node.left, typeh, name1, cc)
            if node.room.typeroom == typeh and node.room.available is True:
=======
    def search_available2(self, r, type):
        if r.room.type == type and r.room.available is True:
            return r.room.id
        elif type < r.romm.id and r.izq is not None:
            return self.buscar(id, r.izq)
        elif id > r.room.id and r.der is not None:
            return self.buscar(id, r.der)
        else:
            return None
        
    def search_available(self, node, typeh, name1, cc):
        if node is not None:
            self.search_available(node.left, typeh, name1, cc)
            if node.room.type == typeh and node.room.available is True:
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03
                if typeh == "VIP":
                    node.room.guest(premium_guest(name1, cc))
                elif typeh == "sencilla":
                    node.room.guest(simple_guest(name1, cc))
                elif typeh == "doble":
                    node.room.guest(double_guest(name1, cc))
                print("Ha reservado la habitacion: ", node.room.id)
                return node.room.reserve()
            self.search_available(node.right,typeh, name1, cc)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
<<<<<<< HEAD
            print(f"ID: {node.room.id}, Tipo: {node.room.typeroom}, Precio: {node.room.price}, Disponibilidad: {'SI' if node.room.available else 'NO'}")
=======
            print(f"ID: {node.room.id}, Tipo: {node.room.type}, Precio: {node.room.price}, Disponibilidad: {'SI' if node.room.available else 'NO'}")
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03
            self.print_inorder(node.right)
                        

    def cost1(self, typeh1, nights):
        if typeh1=="VIP":
            return vip1.cost(nights)
        elif typeh1=="simple":
            return simple1.cost(nights)
        elif typeh1=="doble":
            return double1.cost(nights)
        
    def benefits_room(self, typeh3):
        if typeh3=="VIP":
            return vip1.Benefits()
        elif typeh3=="simple":
            return simple1.Benefits()
        elif typeh3=="doble":
            return double1.Benefits()

    def inf_room(self, typeh2):
        if typeh2=="VIP":
            return vip1.inf()
        elif typeh2=="simple":
            return simple1.inf()
        elif typeh2=="doble":
            return double1.inf()
