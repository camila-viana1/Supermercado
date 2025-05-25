sessoes = {}  # Dicionário global para armazenar as sessões

def cadastrarSessao():
    print("\nCadastro de Sessão > 📂\n")
    id_sessao = input("Informe o ID da sessão: ").strip()
    nome_sessao = input("Informe o nome da sessão: ").strip().capitalize()

    # Verifica se já existe uma sessão com o mesmo ID ou nome
    if id_sessao in sessoes or nome_sessao in sessoes.values():
        print("\nSessão ou ID já cadastrados. ⚠️")
    else:
        sessoes[id_sessao] = nome_sessao
        print("\nSessão cadastrada com sucesso! ✅")

def listarSessoes():
    if not sessoes:
        print("Erro! Nenhuma sessão cadastrada. ⚠️")

    print("\nSESSÕES CADASTRADAS > 📂\n")
    # Exibe todas as sessões cadastradas
    for id_sessao, nome_sessao in sessoes.items():
        print(f"ID: {id_sessao} | Nome da Sessão: {nome_sessao}")