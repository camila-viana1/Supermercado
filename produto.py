import sessao

produtos = {}  # Dicionário global para armazenar os produtos cadastrados

def cadastrarProdutos():
  print("\nCADASTRO DE PRODUTOS > 📑 \n")
  id = input("Informe o ID do produto: ")
  if id in produtos:
    print("Erro, produto já cadastrado! Tente outro ID. ⚠️")
    return

  sessao.listarSessoes()
  id_sessao = input("\nInforme o ID da sessão do produto: ").strip()
  nome_sessao = sessao.sessoes.get(id_sessao) # Busca o nome da sessão pelo ID

  if nome_sessao is None: # Se não encontrar a sessão, avisa e encerra o cadastro
    print("\nSessão não encontrada! ❌")
    return

  nome = input("\nInforme o nome: ").strip().capitalize()
  fornecedor = input("\nInforme o fornecedor: ").strip().capitalize()

  print("\nO produto será vendido por:\n")
  print("1. Unidade > 📦")
  print("2. Peso > ⚖️")
  tipo_venda = input("\nDigite aqui: ")

  if tipo_venda == '1':
      valor = float(input("\nInforme o preço por unidade: R$ "))
  elif tipo_venda == '2':
      valor = float(input("\nInforme o preço por quilo (R$/kg): R$ "))
      peso = int(input("\nInforme o peso do produto em gramas (ex: 1000 para 1kg): "))
  else:
    print("\nOpção inválida! Tente novamente. ❌")
    return

  # Define o estoque em gramas ou unidades, conforme o tipo de venda
  if tipo_venda == '2':
      quantidade_estoque = int(input("\nInforme o estoque total em gramas: "))
  else:
      quantidade_estoque = int(input("\nInforme a quantidade em unidades para o estoque: "))

  print("\nInforme a data de validade > 📅 :\n") 
  dia = input("Dia (DD): ")
  mes = input("Mês (MM): ")
  ano = input("Ano (AAAA): ")

  validade_produto = f"{dia.zfill(2)}/{mes.zfill(2)}/{ano}"
  print(f"\nValidade > ⏲️ : {validade_produto}")

  # Salva todas as informações do produto no dicionário global
  produtos[id] = {
      "nome": nome,
      "fornecedor": fornecedor,
      "sessao": nome_sessao,
      "tipo_venda": tipo_venda,
      "valor": valor,
      "peso": peso if tipo_venda == '2' else "-",
      "quantidade_estoque": quantidade_estoque,
      "validade": validade_produto
  }

  print("\nProduto cadastrado com sucesso! ✅🤩\n")
  print(f"🔵 ID: {id}")
  print(f"🟣 Nome: {nome}")
  print(f"📦 Fornecedor: {fornecedor}")
  print(f"📂 Sessão: {nome_sessao}")
  print(f"💸 Vendido por: {'Peso' if tipo_venda == '2' else 'Unidade'}")
  print(f"💰 Preço: R$ {valor:.2f}")
  if tipo_venda == '2':
      print(f"📏 Peso do Produto: {peso}g")
      print(f"📦 Estoque: {quantidade_estoque}g")
  else:
      print(f"📦 Estoque: {quantidade_estoque} unidade(s)")
  print(f"📅 Validade: {validade_produto}")

def listarProdutos():
  print("\nPRODUTOS CADASTRADOS > 📑")
  if not produtos:
    print("\nErro! Nenhum produto cadastrado. ⚠️")
    return
  
  else:
    # Percorre todos os produtos cadastrados e exibe suas informações
    for id, dados in produtos.items():
      print(f"\n🔵 ID: {id}")
      print(f"🟣 Nome: {dados['nome']}")
      print(f"📦 Fornecedor: {dados['fornecedor']}")
      print(f"📂 Sessão: {dados['sessao']}")
      print(f"🟢 Vendido por: {'Peso' if dados['tipo_venda'] == '2' else 'Unidade'}")
      print(f"💸 Preço: R$ {dados['valor']:.2f}")
      print(f"📦 Estoque: {dados['quantidade_estoque']}")
      print(f"📅 Validade: {dados['validade']}")