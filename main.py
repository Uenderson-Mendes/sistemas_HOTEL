import os
from frigo import frigo

import os
from reserva import Cadastro
from seleciona_quarto import quartos
from servico import dispon
from pagar import check_aut

def Home():
    os.system('clear') 
    op = ''
    while op != 0:
    
        print(f"\n {'-'*30} ")
        print(f"|{' HOTEL MR🙂'.center(26)}|")
        print(f"{'-'*30}")
        print('________________________________')
        print(f"[ 1 ] - {' check in '.center(22)}-|")
        print(f"[ 2 ] -{'Serviço de Quarto'.center(22)} -|")
        print(f"[ 3 ] - {'pagar'.center(22)}-|")
        print(f"[ 4 ] -  {'frigobar'.center(21)}-|")
        print(f"[ 0 ] - {'Sair'.center(22)}-|")
        print('|______________________________|')
        op = str(input("Dgite a opção desejada-> "))


        if op == "1":
            Cadastro.cadstro_cliente()
            quartos.seleciona()
            
    
        elif op == "2":
            dispon.valor_simples()
        elif op == "3":
            check_aut.boleto()
        elif op == "4":
           frigo.menu()
        
        
        elif op == "0":
            
            print('\nOBRIADO VOLTE SEMPRE👍\n')
            exit()
        else:
            return Home()

if __name__ == "__main__":
    Home()