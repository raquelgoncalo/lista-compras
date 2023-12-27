# Você deverá usar inputs do usuário no terminal. Deverá lidar com variáveis, listas, tipos e funções.

# 1️. Crie um programa Python que permita ao usuário inserir itens em uma lista de compras.
#    O programa deve perguntar ao usuário o nome do item e a quantidade desejada, e então adicionar esses detalhes em uma lista.
#    No final, o programa deve exibir a lista completa de compras.
def criar_lista_compras():
  lista_compras = []
  
  nome_item = input("Digie o nome do item ")
  quantidade_item = int(input("Digite a quantidade "))
  
  nova_lista = {
    "nome": nome_item,
    "quantidade": quantidade_item
  }
  
  lista_compras.append(nova_lista)
  print(lista_compras)


# 2. Desenvolva um script Python que calcule a média de um conjunto de notas inseridas pelo usuário.
#    O programa deve pedir ao usuário para inserir o número de notas, receber cada nota, calcular e exibir a média.
def calcular_media_notas():
  notas = []
  
  num_notas = int(input("Digite o número de notas "))
  
  media = sum(notas) / num_notas
  print("A média das notas é: " + media)
  

# Pandas:
# 1. Crie uma lista de dicionários que contenhas seguintes chaves:
#    código da compra, nome do produto, categoria do produto,
#    quantidade comprada, valor unitário comprado, valor total comprado.
lista_dicionarios = [{
  'codigo': '1',
  'nome': 'água mineral',
  'categoria': 'bebidas',
  'quantidade': 12,
  'valor': 2.2,
  'total': 26.4
},
{ 
 'codigo': '2',
  'nome': 'coca-cola',
  'categoria': 'bebidas',
  'quantidade': 3,
  'valor': 10,
  'total': 30
}
]


# 2. Crie um dataframe e retorne: quantidade vendida por produto, ticket médio,
#    quantidade média comprada por compra e total vendido por produto.
# Ao concluir os exercícios, você poderá me enviar o link do github com os repositórios e eu avaliarei pessoalmente cada um.


