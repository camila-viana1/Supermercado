import validade
import produto

vendas = {}

def realizar_venda():
    print("\nRealizar Venda > 🛒\n")
    produto.listarProdutos()
    id = input("Informe o ID do produto: ")
    
    if id not in produto.produtos:
        print("\nProduto não encontrado! ❌")
    
    produto_venda = produto.produtos[id]
    
    print(f"\nProduto encontrado: {produto_venda['nome']} - {produto_venda['fornecedor']}")

    # Separar a validade em dia, mês e ano
    dia, mes, ano = produto_venda['validade'].split('/')
    validade.verificarValidade(dia, mes, ano)
    
    quantidade_venda = int(input("Informe a quantidade a ser vendida: "))
    
    if quantidade_venda > produto_venda['quantidade_estoque']:
        print("\nQuantidade em estoque insuficiente! ❌")
    
    valor_total = quantidade_venda * produto_venda['valor']
    
    print(f"\nValor total da venda: R$ {valor_total:.2f}")
    
    # Atualiza o estoque
    produto_venda['quantidade_estoque'] -= quantidade_venda
    
    # Armazena a venda
    vendas[id] = {
        "nome": produto_venda['nome'],
        "fornecedor": produto_venda['fornecedor'],
        "quantidade_venda": quantidade_venda,
        "valor_total": valor_total
    }
    
    print("\nVenda realizada com sucesso! ✅🤩\n")

    continuarVenda()

def voltarMenu(): #função para retornar ao menu principal
    print("\nDeseja retornar ao menu?")
    print("\n1. Sim")
    print("2. Não")
    voltar = input("\nSelecione a opção desejada: ")

    if voltar in ["1", "sim", "s", "ss"]: #caso a resposta seja sim, retorna ao menu principal
        print("Retornando ao menu... ⌛️\n")
    elif voltar in ["2", "não", "nao", "n", "nn"]: #caso a resposta seja não, encerra o programa
        print("\nFinalizando... Agradecemos por utilizar o Sistema MilaTech! 🤖🛠️")  
        print("Utilizado por: Mercadinho Utilar 🛒✨")
        exit()        
    else:
        print("\n Opção inválida! Tente novamente. ❌") #se a opção não for 1 ou 2, informa ao usuário e encerra a função

def continuarVenda():
    print("\nDeseja continuar a venda?")
    print("\n1. Sim")
    print("2. Não")
    continuar = input("\nSelecione a opção desejada: ")

    if continuar in ["1", "sim", "s", "ss"]: #caso a resposta seja sim, retorna ao menu principal
        print("Retornando ao menu... ⌛️\n")
    elif continuar in ["2", "não", "nao", "n", "nn"]: #caso a resposta seja não, encerra o programa
        print("\nFinalizando... Agradecemos por utilizar o Sistema MilaTech! 🤖🛠️")  
        print("Utilizado por: Mercadinho Utilar 🛒✨")
        exit()        
    else:
        print("\n Opção inválida! Tente novamente. ❌") #se a opção não for 1 ou 2, informa ao usuário e encerra a função