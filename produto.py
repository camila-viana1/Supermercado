import sessao

produtos = {}

def cadastrarProdutos():
  print("\nCADASTRO DE PRODUTOS > 📑 \n")
  id = input("Informe o ID do produto: ")
  if id in produtos:
    print("\nErro, produto já cadastrado! Tente outro ID. ⚠️")
    return

  sessao.listarSessoes()
  id_sessao = input("\nInforme o ID da sessão do produto: ").strip()
  nome_sessao = sessao.sessoes.get(id_sessao) # verifica se o ID da sessão existe

  if nome_sessao is None: # verifica se a sessão existe
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
  else:
    print("\nOpção inválida! Tente novamente. ❌")

  print("\nPeso/Volume do Produto > 📏")
  quantidade_peso = int(input("\nInforme a quantidade (apenas o número): "))
  unidade = input("Informe a unidade (g, kg, ml, L): ").strip().lower()
  if unidade not in ['g', 'kg', 'ml', 'l']:
    print("\nUnidade inválida! Tente novamente. ❌")

  peso = f"{quantidade_peso}{unidade}"
  print(f"\nPeso/Volume > ⚖️ : {peso}")

  quantidade_estoque = int(input("\nInforme a quantidade que deseja adicionar no estoque: "))

  print("\nInforme a data de validade > 📅 :\n") 
  dia = input("Dia (DD): ")
  mes = input("Mês (MM): ")
  ano = input("Ano (AAAA): ")

  validade_produto = f"{dia.zfill(2)}/{mes.zfill(2)}/{ano}"
  print(f"\nValidade > ⏲️ : {validade_produto}")


  # Armazena no dicionário
  produtos[id] = {
      "nome": nome,
      "fornecedor": fornecedor,
      "sessao": nome_sessao,
      "tipo_venda": tipo_venda,
      "valor": valor,
      "peso": peso,
      "quantidade_estoque": quantidade_estoque,
      "validade": validade_produto
  }

  print("\nProduto cadastrado com sucesso! ✅🤩\n")
  print(f"🔵 ID: {id}")
  print(f"📦 Nome: {nome}")
  print(f"📦 Fornecedor: {fornecedor}")
  print(f"📂 Sessão: {nome_sessao}")
  print(f"🛍  Tipo de Venda: {tipo_venda}")
  print(f"💰 Preço: R$ {valor:.2f}")
  print(f"📏 Peso/Volume: {peso}")
  print(f"📦 Estoque: {quantidade_estoque} unidade(s)")
  print(f"📅 Validade: {validade_produto}")

def listarProdutos():
  if not produtos:
    print("\nErro! Nenhum produto cadastrado. ⚠️")
  else:
    for id, dados in produtos.items():
      print(f"ID: {id} | Nome: {dados['nome']} | Fornecedor: {dados['fornecedor']} | Sessão: {dados['sessao']} | Tipo de Venda: {dados['tipo_venda']} | Preço: R$ {dados['valor']:.2f} | Peso/Volume: {dados['peso']} | Estoque: {dados['quantidade_estoque']} unidade(s) | Validade: {dados['validade']}")