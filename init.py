menu = '''

============================================
                  MENU
			
	        [d] Depositar
	        [s] Sacar
	        [e] Extrato
	        [q] Sair
			
============================================

'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_POR_SAQUE = 3


while True:
	
    opcao = input(menu)
	
    if opcao == 'd':
        valor = float(input('Você selecionou a opção depósito. Por favor, informe o valor a ser depositado: '))
		
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Operação realizada com sucesso! Obrigada por utilizar o nosso banco.')
        else:
            print('Operação falhou! O valor informado é invalido') 
			
    elif opcao == 's':
        valor = float(input('Você selecionou a opção Saque. Por favor, informe o valor a ser sacado: '))	

        # Verificação de saques:
		
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque > LIMITE_POR_SAQUE

        if excedeu_saldo:
            print('Falha na operação. você não tem saldo suficiente')
        elif excedeu_limite:
            print('Falha na operação. O valor do saque excede o limite')
        elif excedeu_saque:
            print('Falha na operação. Número máximo de saques excedido')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque +=1
            print('Operação realizada com sucesso! Obrigada por utilizar o nosso banco.')
        else:
            print('Operação falhou! O valor informado é invalido')    

    elif opcao == 'e':
         texto_cabecalho = 'EXTRATO'
         texto_rodape = ''
         print(texto_cabecalho.center(45, '='))
         print('Não foram realizadas movimentações' if not extrato else extrato) #if not extrato verifica se o extrato esta vazio e retorna que não foram feitas movimentações
         print(f'\nSaldo: R$ {saldo:.2f}')
         print(texto_rodape.center(45, '='))   

    elif opcao == 'q':
        print('Obrigado por utilizar nosso banco')
        break
	
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
        
	
	




