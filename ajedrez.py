#AJEDREZ
 #función del tablero
tablero_inicial = [
                ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
                ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
                ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
                
                ]

#función de movimiento
def movimiento():
        
        tablero=tablero_inicial
        
        #selección de pieza
        
        fila_pieza=int(input("Ingresa la fila de la pieza a mover: "))
        columna_pieza=int(input("Ingresa la columna de la pieza a mover: "))
        
        #selección de nueva ubicación
        
        fila_nueva=int(input("Ingresa la nueva fila: "))
        columna_nueva=int(input("Ingresa la nueva columna: "))
        
        #verificar que la elección está dentro del rango
        if 0<=fila_pieza and 0<=columna_pieza and 0<=fila_nueva and 0<=columna_nueva:
                pieza_seleccionada=tablero[fila_pieza][columna_pieza]
                
                tablero[fila_nueva][columna_nueva]=pieza_seleccionada
                tablero[fila_pieza][columna_pieza]="-"
                
                return tablero
        else:
                print("Coordenadas fuera de rango")
                return tablero_inicial
        
        
#función de juego       
def empezar():

        eleccion=input("Hola!¿Quieres jugar ajedrez? (sí/no): ").lower

        #bucle de juego
        if eleccion=='sí':
                print("En cuanto quieras acabar la partida escribe terminar.")
                tablero_actual=tablero_inicial.copy()
                print('Tablero Inicial: ')
                for fila in tablero_inicial:
                        print("\t".join(fila))
                while True:
                        print('¿Qué movimiento quieres hacer?(Utiliza coordenadas)')
                        tablero_actual=movimiento(tablero_actual)
                        for fila in tablero_actual:
                                print("\t".join(fila))
                        terminar=input('¿Quieres terminar la partida?(sí/no)')
                        if terminar=='sí':
                                print('¡Gracias por jugar!')
                                break
                        
                        
        elif eleccion=='no':
              print("¡Has salido!")
              exit() 
        
        else:
                print('opción no válida') 
                return eleccion  
empezar()   
        
               
        

        
        





        










