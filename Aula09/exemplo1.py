import os
os.system("cls")

# EXEMPLO 1 - TRY
try:
    n = int(input("Insira numero: "))
except ValueError as e:
    print(f"\nErro: {e}")
except KeyboardInterrupt:
    print("\nErro encontrado.")
except:
    print("\nErro encontrado.")