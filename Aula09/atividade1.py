import os
os.system("cls")

# ATIVIDADE 1
def pega_numero():
    try:
        num = int(input("Informe um numero: "))
    except ValueError as e:
        print(f"{e} Valor Informado não é válido")
    except KeyboardInterrupt as e:
        print(f"{e} Entrada interrompida.")
    else:
        print(f"Número {num} informado com sucesso")
        return num

num = ""
while num == "":
    num = pega_numero()
