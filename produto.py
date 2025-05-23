produtos = {}

def cadastrarProdutos():
  print("\n\nCADASTRO DE PRODUTOS > 📑 \n")
  id = input("Informe o ID do produto: ")
  if id in produtos:
    print("Erro, produto já cadastrado! Tente outro ID. ⚠️")
    return
  
  nome = input("Informe o nome: ")
  sessao = input("Informe em qual sessão deseja inserir o produto: ")
  valor = input("Informe o valor unitário: ")
  peso = input("Informe o peso do produto: ")
  quantidade = input("Informe a quantidade que deseja adicionar no estoque: ")
  validade = input("Informe a data de validade (formato: DD/MM/AAAA): ")
  
  produtos[id] = {"ID": id, "Nome": nome, "Sessão": sessao, "Valor unitário": valor, "Peso": peso, "Estoque": quantidade, "Data de validade": validade} 
  print("Produto cadastrado com sucesso! ✅🤩\n")
  
cadastrarProdutos()
