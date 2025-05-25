import datetime

validade_dicionario = {}

def verificarValidade(dia, mes, ano):
    # Cria um objeto de data para a validade informada
    data_validade = datetime.datetime(int(ano), int(mes), int(dia))
    hoje = datetime.datetime.now()  # Data atual
    dias_para_validade = (data_validade - hoje).days  # Calcula diferença em dias

    # Exibe alerta conforme a proximidade do vencimento
    if dias_para_validade < 0:
        print("\nAtenção: Produto já está vencido! ⚠️")
    elif dias_para_validade <= 7:
        print(f"\nAtenção: Produto vence em {dias_para_validade} dia(s)! ⚠️")
    elif dias_para_validade <= 30:
        print(f"\nAviso: Produto vence em {dias_para_validade} dias. 🔔")