# Calculadora
# Explicação e Funcionalidade calculacora.sh
  O arquivo calculadora.sh é um script Bash que automatiza a criação, execução e exclusão de um script Python para realizar cálculos matemáticos básicos. Abaixo está a documentação detalhada sobre o funcionamento do script:
# Nome do arquivo:
calculadora.sh
# Funcionalidade principal:
O script verifica se o Python3 está instalado no sistema, cria dinamicamente um script Python que implementa uma calculadora simples, executa esse script e, por fim, exclui o arquivo Python gerado.
Fluxo de execução:
# Verificação do Python3:
  1. O script utiliza o comando command -v python3 para verificar se o Python3 está instalado no sistema.
  2. Caso o Python3 não esteja disponível, uma mensagem de erro é exibida e o script é encerrado.
# Código:
    if ! command -v python3 &> /dev/null; then
    echo "Python3 não está instalado. Instale-o antes de executar este script."
    exit 1
    fi
# Criação do Script Python:
O script Bash utiliza o comando cat com um bloco de redirecionamento (<< EOF ... EOF) para criar um arquivo chamado calculadora.py.
Esse arquivo contém o código da calculadora, que realiza as seguintes operações:

    Adição
    Subtração
    Multiplicação
    Divisão (com verificação de divisão por zero)

O script Python solicita ao usuário quatro números como entrada e oferece um menu para selecionar a operação desejada.
# Código (resumido):
    num1 = input("Digite o primeiro número: ")
    # Conversão de entrada e cálculo das operações
    print("\nEscolha a operação que deseja realizar:")
    print("1 - Adição")
    # Exibe o resultado com base na operação escolhida
# Execução do Script Python:
  Após criar o arquivo calculadora.py, o script o executa utilizando o comando python3.
# Código:
    python3 calculadora.py
# Remoção do Script Python:
Após a execução do script Python, o arquivo calculadora.py é removido automaticamente, evitando a criação de arquivos desnecessários.
# Código:
    rm calculadora.py
# Requisitos:
Python3: O script só funciona se o Python3 estiver instalado no sistema.
Permissões de execução: O script Bash precisa ter permissão de execução. Use o comando chmod +x calculadora.sh para torná-lo executável.
# Explicação do Código Calculadora_Phytin.py
O código no arquivo Calculadora_Phyton.py implementa uma calculadora básica que realiza operações matemáticas entre quatro números fornecidos pelo usuário.
O programa solicita ao usuário que insira quatro números, utilizando a função input().
Esses valores inicialmente são lidos como texto (strings).
Os valores de entrada são convertidos para números inteiros utilizando a função int().
Isso permite que eles sejam usados em operações matemáticas.
O código calcula os resultados de quatro operações matemáticas básicas:
 - Adição: soma de todos os números.
 - Subtração: subtração sequencial dos números.
 - Multiplicação: multiplicação de todos os números.
 - Divisão: divisão do primeiro número pelo segundo (apenas se o divisor não for zero, caso contrário, exibe uma mensagem de erro).
O programa exibe ao usuário um menu com as quatro operações disponíveis.
Ele solicita que o usuário escolha uma delas digitando o número correspondente.
O programa verifica a escolha do usuário com uma série de instruções if-elif-else:
   - Se o usuário digitar 1, exibe o resultado da soma.
   - Se 2, exibe o resultado da subtração.
   - Se 3, mostra o resultado da multiplicação.
   - Se 4, exibe o resultado da divisão ou uma mensagem de erro (caso o divisor seja zero).
   - Para qualquer outro valor, exibe uma mensagem de "Opção inválida".
