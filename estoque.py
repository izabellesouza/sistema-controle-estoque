produtos = []


def encontrar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto

    return None

#funcao cadastro:

def cadastrar_produto(produtos):
    print("\n--- CADASTRAR PRODUTO ---")

    nome = input("Nome do produto: ")

    if encontrar_produto(produtos, nome) is not None:
        print("Produto já cadastrado.")
        return

    try:
        preco = float(input("Preço: R$ ").replace(",", "."))
        quantidade = int(input("Quantidade: "))

        if preco < 0 or quantidade < 0:
            print("Preço e quantidade não podem ser negativos.")
            return

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Preço ou quantidade inválidos.")

#funcao listar produtos:

def listar_produtos(produtos):
    print("\n--- PRODUTOS CADASTRADOS ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )

#funcao buscar produto:

def buscar_produto(produtos):
    print("\n--- BUSCAR PRODUTO ---")

    nome = input("Digite o nome do produto: ")

    produto = encontrar_produto(produtos, nome)

    if produto is None:
        print("Produto não encontrado.")
    else:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

#funcao de entrada de estoque:

def entrada_estoque(produtos):
    print("\n--- ENTRADA DE ESTOQUE ---")

    nome = input("Nome do produto: ")
    produto = encontrar_produto(produtos, nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade para entrada: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        produto["quantidade"] += quantidade

        print("Entrada realizada com sucesso!")
        print(f"Nova quantidade: {produto['quantidade']}")

    except ValueError:
        print("Quantidade inválida.")

#funcao saída de estoque

def saida_estoque(produtos):
    print("\n--- SAÍDA DE ESTOQUE ---")

    nome = input("Nome do produto: ")
    produto = encontrar_produto(produtos, nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade para saída: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        if quantidade > produto["quantidade"]:
            print("Estoque insuficiente.")
            print(f"Quantidade disponível: {produto['quantidade']}")
            return

        produto["quantidade"] -= quantidade

        print("Saída realizada com sucesso!")
        print(f"Quantidade restante: {produto['quantidade']}")

    except ValueError:
        print("Quantidade inválida.")

#funcao calcula valor total do estoque

def calcular_valor_estoque(produtos):
    print("\n--- VALOR DO ESTOQUE ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return 0

    valor_total = 0

    for produto in produtos:
        valor_produto = produto["preco"] * produto["quantidade"]
        valor_total += valor_produto

        print(
            f"{produto['nome']}: "
            f"R$ {valor_produto:.2f}"
        )

    print(f"\nValor total do estoque: R$ {valor_total:.2f}")

    return valor_total

#desafio adicional

def mostrar_estatisticas(produtos):
    print("\n--- ESTATÍSTICAS DO ESTOQUE ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    maior_quantidade = produtos[0]
    menor_quantidade = produtos[0]
    mais_caro = produtos[0]

    for produto in produtos:
        if produto["quantidade"] > maior_quantidade["quantidade"]:
            maior_quantidade = produto

        if produto["quantidade"] < menor_quantidade["quantidade"]:
            menor_quantidade = produto

        if produto["preco"] > mais_caro["preco"]:
            mais_caro = produto

    print(
        f"Produto com maior quantidade: "
        f"{maior_quantidade['nome']} "
        f"({maior_quantidade['quantidade']} unidades)"
    )

    print(
        f"Produto com menor quantidade: "
        f"{menor_quantidade['nome']} "
        f"({menor_quantidade['quantidade']} unidades)"
    )

    print(
        f"Produto mais caro: "
        f"{mais_caro['nome']} "
        f"(R$ {mais_caro['preco']:.2f})"
    )

    print("\nProdutos com estoque baixo:")

    encontrou = False

    for produto in produtos:
        if produto["quantidade"] < 5:
            print(
                f"- {produto['nome']}: "
                f"{produto['quantidade']} unidades"
            )
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")
def menu():
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Entrada de estoque")
        print("5 - Saída de estoque")
        print("6 - Mostrar valor total do estoque")
        print("7 - Estatísticas do estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            entrada_estoque(produtos)
        elif opcao == "5":
            saida_estoque(produtos)
        elif opcao == "6":
            calcular_valor_estoque(produtos)
        elif opcao == "7":
            mostrar_estatisticas(produtos)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


menu()