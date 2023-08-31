from Habitaciones import *
from Hotel import TreeHotel

Tree=TreeHotel()
Tree.add(simple(101, True))
<<<<<<< HEAD
Tree.add(double(302, True))
Tree.add(vip(303, False))
Tree.add(simple(304, True))
Tree.add(double(305, True))
Tree.add(double(102, True))
Tree.add(vip(103, True))
Tree.add(vip(401, False))
Tree.add(simple(104, True))
Tree.add(double(105, True))
Tree.add(vip(202, True))
Tree.add(simple(203, True))
Tree.add(double(204, False))
Tree.add(vip(205, True))
Tree.add(simple(301, True))
Tree.add(double(402, True))
Tree.add(vip(201, True))
=======
Tree.add(double(111, True))
Tree.add(vip(112, False))
Tree.add(simple(113, True))
Tree.add(double(114, True))
Tree.add(double(102, True))
Tree.add(vip(103, True))
Tree.add(vip(115, False))
Tree.add(simple(104, True))
Tree.add(double(105, True))
Tree.add(vip(106, True))
Tree.add(simple(107, True))
Tree.add(double(108, False))
Tree.add(vip(109, True))
Tree.add(simple(110, True))
Tree.add(double(105, True))
Tree.add(vip(106, True))
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03



menu= '''
<<<<<<< HEAD
        Bienvenido al hotel Miami
=======
Bienvenido al hotel Miami
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03
Elije una opcion
1.Ver todas las habitaciones del hotel
2.Reservar una habitacion
3.Calcular precio
4.Ver informacion de la habitacion
5.Ver Beneficios de la habitacion
6.Salir
'''  

op = 0
while op != 6 and op>=0 and op <=5:
    op=int(input(menu))
    if op==1:
        Tree.print_inorder(Tree.root)
    elif op==2:
<<<<<<< HEAD
        name1=input("Ingrese su nombre: ")
        cc=int(input("Ingrese su cedula: "))
        typeroom=input("¿Que tipo de habitacion desea? ")
        Tree.search_available(Tree.root, typeroom, name1, cc)
    elif op==3:
        typeh1=input("¿Que tipo de habitacion desea? ")
        nights=int(input("Cuantos dias desea quedarse? "))
        print(f"Recuerde que si se queda mas de 3 dias tendra un descuento \nEl costo total de {nights} dias es de {Tree.cost1(typeh1, nights)}")
    elif op==4:
        typeh2=input("De que tipo de habitacion desea ver informacion? ")
        Tree.inf_room(typeh2)
    elif op==5:
        typeh3=input("De que habitacion desea ver los beneficios? ")
        Tree.benefits_room(typeh3)
=======
        name1=input("Ingrese su nombre ")
        cc=int(input("Ingrese su cedula "))
        typeroom=input("¿Que tipo de habitacion desea? ")
        Tree.search_available(Tree.root, typeroom, name1, cc)
    elif op==3:
        typeh1=input("Que tipo de habitacion desea? ")
        nights=int(input("Cuantos dias desea quedarse? "))
        print(f"Recuerde que si se queda mas de 3 dias tendra un descuento \nEl costo total de {nights} dias es de {Tree.cost1(typeh1, nights)}")
    elif op==4:
        typeh2=input("De que tipo de habitacio desea ver informacion? ")
        Tree.inf_room(typeh2)
    elif op==5:
        typeh3=input("De que habitacion desea ver los beneficios? ")
        Tree.inf_room(typeh3)
>>>>>>> aafe264dfecc574f102825f3a54491313b871d03
        