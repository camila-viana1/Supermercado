import datetime

validade_dicionario = {}

def verificarValidade(dia, mes, ano): # Verifica a validade do produto e alerta se estiver próxima

  data_validade = datetime.datetime(int(ano), int(mes), int(dia))
  hoje = datetime.datetime.now()
  dias_para_validade = (data_validade - hoje).days

  if dias_para_validade < 0:
      print("\n⚠️ Atenção: Produto já está vencido!")
  elif dias_para_validade <= 7:
      print(f"\n⚠️ Atenção: Produto vence em {dias_para_validade} dia(s)!")
  elif dias_para_validade <= 30:
      print(f"\n🔔 Aviso: Produto vence em {dias_para_validade} dias.")