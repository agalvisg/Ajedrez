#AJEDREZ
 #función del tablero
tablero_inicial = [
                ["_","A","B","C","D","E","F","G","H","_"],
                ["1","♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜","1"],
                ["2","♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟","2"],
                ["3","_", "_", "_", "_", "_", "_", "_", "_","3"],
                ["4","_", "_", "_", "_", "_", "_", "_", "_","4"],
                ["5","_", "_", "_", "_", "_", "_", "_", "_","5"],
                ["6","_", "_", "_", "_", "_", "_", "_", "_","6"],
                ["7","♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙","7"],
                ["8","♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖","8"],
                ["_","A","B","C","D","E","F","G","H","_"]
                ]


def movimiento():
        pieza_seleccionada=tablero_inicial('fila'int(input),'columna'int(input))
        nueva_posicion=tablero_inicial('fila'int(input),'columna'int(input))
        tablero_nuevo=tablero_inicial.reverse(pieza_seleccionada,nueva_posicion)
        print(tablero_nuevo)


def empezar():

        eleccion=input("Hola!¿Quieres jugar ajedrez? (sí/no): ")
        print(eleccion)
        if eleccion=='sí':
        # Imprimir el tablero inicial
                for fila in tablero_inicial:
                        print("\t".join(fila))
                print('¿Qué movimiento quieres hacer?(ingrésalo mediante coordenadas)')
                movimiento()

        elif eleccion=='no':
              print("¡Has salido!")
              exit()    
empezar()   
        
               
        

        
        





        










