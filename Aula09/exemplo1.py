import os
os.system("cls")

# EXEMPLO 1.1 - TRY
try:
    n = int(input("Insira numero: "))
except (ValueError, KeyboardInterrupt) as e:
    print(f"\nErro: {e}")
except:
    print("\nErro encontrado.")

# EXEMPLO 1.2
try:
    txt = input("Informe o nome: ")[0]
except IndexError:
    print("Precisa digitar algo!")
else:
    print(f"Olá, {txt}!")
finally:
    print("Sempre executado")
