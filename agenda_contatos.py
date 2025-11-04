contatos = []

# funções

def adicionar_contato(contatos,nome_contato,telefone_contato,email_contato):
  contato = {
        "nome": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False
    }
  contatos.append(contato)

  return

def listar_contatos(contatos):
  for indice,contato in enumerate(contatos, start=1):
      
    if contato["favorito"] == True: 
        status = "★" 
    else: status = " "

    print(f"\nContato: {indice} {status}")
    print(f"Nome: {contato['nome']}")
    print(f"Telefone: {contato['telefone']}")
    print(f"Email: {contato['email']}")
    print()

  return

def editar_contato(contatos,indice,novo_nome_contato,novo_telefone_contato,novo_email_contato):
    indice_contato_ajustado = int(indice) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print("\nContato Atualizado!")
    else:
        print("\nÍndice de contato inválido.")
    
    return
def adicionar_favorito(contatos,indice):
    indice_contato_ajustado = int(indice) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print("\nContato Favoritado!")
    else:
        print("\nÍndice de contato inválido.")

    return

def listar_favoritos(contatos):
   for indice,contato in enumerate(contatos, start=1):
      
    if contato["favorito"] == True: 
        status = "★" 
        print(f"\nContato: {indice} {status}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print()
    else: status = " "
   return

def excluir_contato(contatos,indice):
   indice_contato_ajustado = int(indice) - 1
   
   if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"\nContato '{contato_removido['nome']}' excluído com sucesso!")
        

while True:
  print("\n AGENDA DE CONTATOS \n")
  print("[1] Adicionar contato")
  print("[2] Listar contatos")
  print("[3] Editar contato")
  print("[4] Adicionar contato favorito")
  print("[5] Listar contatos favoritos")
  print("[6] Excluir contato")
  print("[7] Sair \n")

  escolha = input("Escolha uma opção: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato:")

    adicionar_contato(contatos,nome,telefone,email)

  elif escolha == "2":
    listar_contatos(contatos)
  elif escolha == "3":
    listar_contatos(contatos)
    indice_contato = input("\nDigite o índice do contato que deseja editar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")

    editar_contato(contatos,indice_contato,novo_nome,novo_telefone,novo_email)
  elif escolha == "4":
    listar_contatos(contatos)
    indice_contato = input("\nDigite o índice do contato que deseja favoritar: ")

    adicionar_favorito(contatos,indice_contato)

  elif escolha == "5":
    listar_favoritos(contatos)

  elif escolha == "6":
    listar_contatos(contatos)
    indice_contato = input("\nDigite o índice do contato que deseja excluir: ")
    excluir_contato(contatos,indice_contato)
  elif escolha == "7":
     break

