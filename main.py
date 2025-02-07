### Piedra papel o tijera ###
#Mensaje de bienvenida
print("***BIENVENIDO A PIEDRA PAPEL O TIJERA***")
#Importamos modulos
import random #para generar la seleccion aleatoria del computer
import os #para usar el comando de limpiar consola
#Definiendo una tupla para listar las opciones
options = ('piedra','papel','tijera')
#Le pedimos al usuario su nombre
username = input("Ingresa tu nombre: ")
#Inicializar contadores de emptes, victorias, derrotas y rounds
win_game = 0
lose_game = 0
keep = True #declarar variable que condicion la continuidad del ciclo
while keep == True:
    rounds = 1
    win_round = 0
    lose_round = 0
    tie_round = 0
    while win_round < 2 and lose_round < 2:
        os.system("clear")
        #Inicia el roud
        print('*' * 20)
        print(f"ROUND {rounds}, FIGHT!")
        print('*' * 20)
        user_input = input("Chose your weapon!(Piedra, papel o tijera): ")
        #Convertimos el input del usuario a letras minusculas para evitar errores en la comparación
        user_op = str.lower(user_input)
        print(f"{username}: {user_op}")
    
        #Asignamos de manera aleatoria la eleccion del computer
        pc_op = random.choice(options)
    
        #Validamos que el input del usuario sea correcto, si es incorrecto damos por ganador a computer por defecto
        if not user_op in options:
            print("Opcion invalida!\nComputer wins!")
            lose_round += 1
        elif user_op == pc_op: #caso empate
            print(f"Computer: {pc_op}")
            print("EMPATE!")
            tie_round += 1
        elif user_op == 'piedra': #caso usuario elige piedra
            if pc_op == 'papel': # caso piedra vs papel
                print(f"Computer: {pc_op}")
                print("Papel le gana a piedra\nCOMPUTER WINS!")
                lose_round += 1
            elif pc_op == 'tijera': #caso piedra vs tijera
                print(f"Computer: {pc_op}")
                print(f"Piedra le gana a tijera\n{username} WINS!")
                win_round += 1
        elif user_op == 'papel': #caso usuario elige papel
            if pc_op == 'piedra': #caso papel vs piedra
                print(f"Computer: {pc_op}")
                print(f"Papel le gana a piedra\n{username} WINS!")
                win_round += 1
            elif pc_op == 'tijera': # caso papel vs tijera
                print(f"Computer: {pc_op}")
                print("Tijera le gana a papel\nCOMPUTER WINS!")
                lose_round += 1
        elif user_op == 'tijera': #caso usuario elige tijera
            if pc_op == 'piedra': #caso tijera vs piedra
                print(f"Computer: {pc_op}")
                print("Piedra le gana a tijera\nCOMPUTER WINS!")
                lose_round += 1
            elif pc_op == 'papel': #caso tijera vs papel
                print(f"Computer: {pc_op}")
                print(f"Tijera le gana a papel\n{username} WINS!")
                win_round += 1
                
        #Mostrar contadores
        print(f"\n{username}: {win_round}\nComputer: {lose_round}\nEmpates: {tie_round}")
        
        #Contar Round
        rounds += 1
        
        input("\nPresiona cualquier tecla para continuar...") #pausa para visualizar valores en consola

    if win_round == 2:
        print("\n")
        print('*' * 10)
        print(f"{username} WINS!")
        print('*' * 10)
        win_game += 1
    elif lose_round == 2:
        print("\n")
        print('*' * 20)
        print("COMPUTER WINS!")
        print('*' * 20)
        lose_game += 1
        
    print(f"\n{username}: {win_game}\nComputer: {lose_game}")

    #Preguntar si seguir jugando
    valid = False
    while valid == False:
        choice = str.lower(input("\n¿Seguir jugando? (Y/N): "))
        if choice == 'y':
            keep = True
            valid = True
        elif choice == 'n':
            keep = False
            valid = True
        else:
            print("Opcion invalida, vuelve a intentar")