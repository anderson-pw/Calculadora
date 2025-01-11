# Passo 1: Recebendo 4 números de entrada do usuário
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")
num4 = input("Digite o quarto número: ")

# Passo 2: Convertendo os valores para inteiros
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

# Passo 3: Implementando as operações matemáticas
soma = num1 + num2 + num3 + num4
subtracao = num1 - num2 - num3 - num4
multiplicacao = num1 * num2 * num3 * num4
divisao = num1 / num2 if num2 != 0 else "Erro: divisão por zero"

# Passo 4: Adicionando uma condicional para o tipo de operação
print("\nEscolha a operação que deseja realizar:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número correspondente à operação: ")

# Passo 5: Exibindo o resultado conforme a escolha do usuário
if operacao == "1":
    print(f"O resultado da soma é: {soma}")
elif operacao == "2":
    print(f"O resultado da subtração é: {subtracao}")
elif operacao == "3":
    print(f"O resultado da multiplicação é: {multiplicacao}")
elif operacao == "4":
    print(f"O resultado da divisão é: {divisao}")
else:
    print("Opção inválida! Tente novamente.")
