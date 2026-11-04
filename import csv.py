import csv

ARQUIVO = "medicamentos.csv"


def carregar():
    medicamentos = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for medicamento in leitor:
                medicamentos.append(medicamento)

    except FileNotFoundError:
        pass

    return medicamentos


def salvar(medicamentos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "categoria", "quantidade"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(medicamentos)

    return True


def buscar(medicamentos, nome):
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return medicamento

    return None


medicamentos = carregar()

while True:
    print("\n--- CADASTRO DE MEDICAMENTOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        quantidade = input("Quantidade: ")

        medicamento = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        }

        medicamentos.append(medicamento)
        salvar(medicamentos)

        print("Medicamento cadastrado!")

    elif opcao == "2":
        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")
        else:
            for medicamento in medicamentos:
                print(
                    medicamento["nome"],
                    "-",
                    medicamento["categoria"],
                    "-",
                    medicamento["quantidade"]
                )

    elif opcao == "3":
        nome = input("Digite o nome do medicamento: ")

        resultado = buscar(medicamentos, nome)

        if resultado:
            print("Encontrado:", resultado)
        else:
            print("Medicamento não encontrado.")

    elif opcao == "4":
        salvar(medicamentos)
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida.")