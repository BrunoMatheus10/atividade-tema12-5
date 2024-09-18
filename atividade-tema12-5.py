# Inicializa variáveis para soma e contagem de números pares
soma_pares = 0  # Variável para armazenar a soma dos números pares
contagem_pares = 0  # Variável para contar quantos números pares foram digitados

# Inicializa a variável para o número digitado
numero = int(input("Digite um número inteiro (0 para terminar): "))  # Solicita ao usuário que digite o primeiro número

# Laço while para continuar lendo números até que o usuário digite zero
while numero != 0:  # Continua o laço enquanto o número digitado não for zero
    # Verifica se o número é par
    if numero % 2 == 0:  # Verifica se o número é divisível por 2 (ou seja, se é par)
        soma_pares += numero  # Adiciona o número à soma dos pares
        contagem_pares += 1  # Incrementa a contagem de números pares

    # Solicita o próximo número
    numero = int(
        input("Digite um número inteiro (0 para terminar): "))  # Solicita ao usuário que digite o próximo número

# Calcula a média dos números pares, se houver algum
if contagem_pares > 0:  # Verifica se algum número par foi digitado
    media_pares = soma_pares / contagem_pares  # Calcula a média dos números pares
    print("A média dos números pares é:", media_pares)  # Imprime a média dos números pares
else:
    print("Nenhum número par foi digitado.")  # Imprime uma mensagem se nenhum número par foi digitado
