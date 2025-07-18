def calculadora():
    while True:
        try:
            print("=== CALCULADORA ===")
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            op = input("Escolha a operação (+, -, *, / ou 'sair'): ")

            if op == "sair":
                break
            elif op == "+":
                print(f"Resultado: {a + b}")
            elif op == "-":
                print(f"Resultado: {a - b}")
            elif op == "*":
                print(f"Resultado: {a * b}")
            elif op == "/":
                if b != 0:
                    print(f"Resultado: {a / b}")
                else:
                    print("Erro: divisão por zero.")
            else:
                print("Operação inválida.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

calculadora()
