def calculator():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            op = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))
        
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Erro! Divisão por zero.")
                    continue
            else:
                print("Operação inválida.")
                continue
            
            print(f"Resultado: {result}")
        
            next_calculation = input("Deseja fazer outro cálculo? (s/n): ")
            if next_calculation.lower() != 's':
                break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    calculator()
