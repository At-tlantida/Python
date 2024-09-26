import random

def jogo_pedra_papel_tesoura():

    opcoes = ["pedra", "papel", "tesoura"]
    placar = {"Computador": 0, "Usuario": 0}

    while True:
    
        opcao_usuario = input(" Entre com pedra, papel ou tesoura: ") .lower()
        opcao_pc = random.choice(opcoes)
    
        if opcao_usuario not in opcoes:
            print("Jogada inválida. Tente Novamente.")
            continue
    
        if opcao_pc == opcao_usuario:
            print("Empate!")
            
        elif opcao_pc == "pedra" and opcao_usuario == "papel" or \
             opcao_pc == "papel" and opcao_usuario == "tesoura" or \
             opcao_pc == "tesoura" and opcao_usuario == "pedra":
            print("Vc Venceu!")
            placar["Computador"] += 1
            
        else:
            print("Computador Ganhou!")
            placar["Usuario"] += 1
            
        print(f"Placar Usuário {placar['Usuario']} ponto(s) X Placar PC {placar['Computador']} ponto(s) ")
        
        continuar = input("Entre com S para continuar ou N para parar: ") .lower()
        
        if continuar != "s":
            break
    
    
jogo_pedra_papel_tesoura()
