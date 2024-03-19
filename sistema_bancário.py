menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
 => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    
    opcao = input(menu)
    
    if opcao == "d":
        print("*****************Depósito*********************")
        valor = float(input("Qual valor do depósito? "))
        if valor < 0:
            print("Valor indisponivel, favor colocar somentes valores disponiveis")
        
        else:
            saldo = saldo + valor
            extrato += f"Deposito de: {valor:.2f}\n"
           
            
        
    
    elif opcao == "s":
        
        print("******************Sacar***********************")
        valor = float(input("Qual valor de saque? "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Seu saque excedeu o saldo, tente novamente!")
        elif excedeu_limite:
            print("Seu saque excedeu o limite possível, tente novamente!")
        
        elif excedeu_saques:
            print("Seu saque excedeu o limite de saques, favor tente novamente amanhã!")
        else:
            saldo = saldo - valor
            extrato += f"Saque realizado de: {valor:.2f}\n"
            numero_saques += 1
            
            
        
        
       
        
        
    elif opcao == "e":
        print("******************Extrato*********************")
        print(extrato)
        print(f"Seu saldo é de {saldo:.2f}")
    
        
        
    elif opcao == "q":
        print("Obrigado por usar nosso banco! Até breve!")

        break
    
    else:
        print("Opção Inválida, tente novamente!")
        
        