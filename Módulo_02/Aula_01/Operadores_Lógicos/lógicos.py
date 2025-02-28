saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite) # Operador "E"

print(saldo >= saque or saque <= limite) # Operador "Ou"

print(not saldo < limite) # Operador de Negação

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saldo)) # Parênteses é uma boa prática!