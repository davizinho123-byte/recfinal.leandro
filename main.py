import csv

ARQUIVO = "medicamentos.csv"

# Carrega os medicamentos do arquivo CSV
def carregar():
    medicamentos = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for medicamento in leitor:
                medicamentos.append(medicamento)

    except FileNotFoundError:
        pass

    return medicamentos

# Salva os medicamentos no arquivo CSV
def salvar(medicamentos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "categoria", "quantidade"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(medicamentos)

    return True

# Cadastra um novo medicamento
def cadastrar(medicamentos):
    nome = input("Nome do medicamento: ")
    categoria = input("Categoria: ")
    quantidade = input("Quantidade em estoque: ")

    if not nome or not categoria:
        print("Preencha todos os campos!")
        return medicamentos

    if not quantidade.isdigit():
        print("Digite uma quantidade válida!")
        return medicamentos

    novo_medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    medicamentos.append(novo_medicamento)
    salvar(medicamentos)
    print("Medicamento cadastrado com sucesso!")
    return medicamentos

# Lista os medicamentos cadastrados
def listar(medicamentos):
    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        for medicamento in medicamentos:
            print("----------------------")
            print("Nome:", medicamento[0])
            print("Categoria:", medicamento[1])
            print("Quantidade:", medicamento[2])

    return medicamentos

# Busca um medicamento pelo nome
def buscar(medicamentos, nome):
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return medicamento

    return None


medicamentos = carregar()

while True:
    print("\n===== SISTEMA DE MEDICAMENTOS =====")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        medicamentos = cadastrar(medicamentos)

    elif opcao == "2":
        listar(medicamentos)

    elif opcao == "3":
        nome = input("Digite o nome do medicamento: ")
        resultado = buscar(medicamentos, nome)

        if resultado:
            print("Medicamento encontrado!")
            print("Nome:", resultado["nome"])
            print("Categoria:", resultado["categoria"])
            print("Quantidade:", resultado["quantidade"])
        else:
            print("Medicamento não encontrado.")

    elif opcao == "4":
        salvar(medicamentos)
        print("Dados salvos. Programa encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")