import produto
import sessao
import vendas
from datetime import datetime

print("\n\n")
print("--- Mercadinho Utilar 🛒✨")
print("Seja bem-vindo(a) ao Sistema MilaTech! 🤖🛠️\n")


def verificarValidade(dia, mes, ano):
    data_validade = datetime(int(ano), int(mes), int(dia))
    hoje = datetime.now()
    # ...


while True:
    print("MENU PRINCIPAL > 🏠\n")
    print("1. Cadastrar Sessão")
    print("2. Cadastrar Produto")
    print("3. Listar Produtos")
    print("4. Listar Sessões")
    print("5. Realizar Venda")
    print("6. Sair")
    pergunta = input("\nEscolha uma opção: ")

    match pergunta:
        case "1":
            sessao.cadastrarSessao()
            vendas.voltarMenu()
        case "2":
            produto.cadastrarProdutos()
            vendas.voltarMenu()
        case "3":
            produto.listarProdutos()
            vendas.voltarMenu()
        case "4":
            sessao.listarSessoes()
            vendas.voltarMenu()
        case "5":
            vendas.realizar_venda()
        case "6":
            print("\nSaindo do sistema... Até logo! 👋")
            exit()
        case _:
            print("\nOpção inválida! Tente novamente. ❌")
            vendas.voltarMenu()