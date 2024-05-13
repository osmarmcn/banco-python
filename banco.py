



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
    

while True:

    op = int(input("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
        selecione uma opção:            
    """)) 
   
    if op == 1:
        valor = float(input('valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}'
        
        else:
         print('valor invalido!')

    elif op == 2:
      
        valor_saque = float(input('informe o valor do saque:R$ '))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(" O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif op == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif op == 4:
        break

    else:
        print("por favor selecione novamente a operação desejada.")



    

