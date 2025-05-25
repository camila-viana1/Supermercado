import validade
import produto

vendas = {}  # Dicionário para registrar vendas, se desejar expandir futuramente

def realizar_venda():
    carrinho = []  # Lista para armazenar os itens da venda atual
    valor_total_compra = 0  # Soma total da compra

    while True:
        produto.listarProdutos()
        print("\nVENDAS > 🛒\n")
        id = input("Informe o ID do produto: ")
        if id not in produto.produtos:
            print("\nProduto não encontrado! ❌")
            continue

        produto_venda = produto.produtos[id]
        print(f"\nProduto encontrado: {produto_venda['nome']} - {produto_venda['fornecedor']}")

        # Separa a data de validade para verificação
        dia, mes, ano = produto_venda['validade'].split('/')
        validade.verificarValidade(dia, mes, ano)

        # Solicita a quantidade conforme o tipo de venda
        if produto_venda['tipo_venda'] == '2':
            quantidade_venda = int(input("\nInforme a quantidade em gramas a ser vendida: "))
        else:
            quantidade_venda = int(input("\nInforme a quantidade a ser vendida: "))

        # Soma a quantidade já adicionada ao carrinho para esse produto
        quantidade_no_carrinho = sum(item['quantidade'] for item in carrinho if item['id'] == id)

        # Verifica se há estoque suficiente considerando o que já está no carrinho
        if quantidade_venda + quantidade_no_carrinho > produto_venda['quantidade_estoque']:
            print(f"\nQuantidade em estoque insuficiente! Você já adicionou {quantidade_no_carrinho} desse produto ao carrinho e só há {produto_venda['quantidade_estoque']} disponível. ❌")
            continue

        # Calcula o valor total do item conforme o tipo de venda
        if produto_venda['tipo_venda'] == '2':
            valor_total = (quantidade_venda / 1000) * produto_venda['valor']
        else:
            valor_total = quantidade_venda * produto_venda['valor']

        # Adiciona o item ao carrinho (não retira do estoque ainda)
        carrinho.append({
            "id": id,
            "nome": produto_venda['nome'],
            "quantidade": quantidade_venda,
            "preco_unitario": produto_venda['valor'],
            "preco_total": valor_total,
            "tipo_venda": produto_venda['tipo_venda']
        })

        valor_total_compra += valor_total
        print("\nProduto adicionado ao carrinho! ✅")

        print("\nDeseja adicionar mais produtos ao carrinho?")
        print("\n1. Sim")
        print("2. Não")
        continuar = input("\nSelecione a opção desejada: ")

        if continuar in ["1", "sim", "s", "ss"]:
            print("Retornando ao menu... ⌛️\n")
        elif continuar in ["2", "não", "nao", "n", "nn"]:
            print("\nFinalizando a venda... 🛒💳")
            break

    # Exibe resumo do carrinho ao final da venda
    print("\nResumo da Venda > 🛒\n")
    for item in carrinho:
        if item['tipo_venda'] == '2':
            print(f"{item['nome']} > {item['quantidade']}g > R$ {item['preco_unitario']:.2f}/kg - Total: R$ {item['preco_total']:.2f}")
        else:
            print(f"{item['nome']} > {item['quantidade']} un > R$ {item['preco_unitario']:.2f}/un - Total: R$ {item['preco_total']:.2f}")
    print(f"\n💰 TOTAL DA COMPRA: R$ {valor_total_compra:.2f}")

    # Após a confirmação, desconta o estoque dos produtos vendidos
    for item in carrinho:
        produto.produtos[item['id']]['quantidade_estoque'] -= item['quantidade']

    print("\nVenda realizada com sucesso! ✅🤩\n")
    voltarMenu()

def voltarMenu():
    print("\nDeseja retornar ao menu?")
    print("\n1. Sim")
    print("2. Não")
    voltar = input("\nSelecione a opção desejada: ")

    # Se a resposta for sim, apenas retorna ao menu (faz nada)
    if voltar in ["1", "sim", "s", "ss"]:
        print("Retornando ao menu... ⌛️\n")
    # Se a resposta for não, encerra o programa
    elif voltar in ["2", "não", "nao", "n", "nn"]:
        print("\nFinalizando... Agradecemos por utilizar o Sistema MilaTech! 🤖🛠️")  
        print("Utilizado por: Mercadinho Utilar 🛒✨")
        exit()        
    else:
        print("\n Opção inválida! Tente novamente. ❌")

# def continuarVenda():
#     print("\nDeseja continuar a venda?")
#     print("\n1. Sim")
#     print("2. Não")
#     continuar = input("\nSelecione a opção desejada: ")

#     if continuar in ["1", "sim", "s", "ss"]:
#         print("Retornando ao menu... ⌛️\n")
#     elif continuar in ["2", "não", "nao", "n", "nn"]:
#         print("\nFinalizando... Agradecemos por utilizar o Sistema MilaTech! 🤖🛠️")  
#         print("Utilizado por: Mercadinho Utilar 🛒✨")
#         exit()        
#     else:
#         print("\n Opção inválida! Tente novamente. ❌")