#RM 98423. Matheus Xavier Silva De Toledo. 1ESPI

#Cadastro do cliente
def print_cliente_info(cliente):
    print("Seja bem-vindo(a) à Vinheira Agnello {}!".format(cliente["nome"]))
    print("Idade: {}".format(cliente["idade"]))
    print("Endereço: {}".format(cliente["endereco"]))
    print("Endereço de entrega: {}".format(cliente["endereco_entrega"]))


#Verificando se os dados do cliente estão corretos
def verificar_dados(cliente):
    confirmacao = input("Seus dados estão corretos? (sim/não): ")
    if confirmacao.lower() == "sim":
        print("Ótimo, seus dados foram confirmados!")
    elif confirmacao.lower() == "não":
        print("Por favor, insira novamente seus dados:")
        cliente["nome"] = input("Nome completo: ")
        cliente["idade"] = input("Idade: ")
        cliente["endereco"] = input("Endereço: ")
        cliente["endereco_entrega"] = input("Endereço de entrega: ")
        print_cliente_info(cliente)
        verificar_dados(cliente)
    else:
        print("Opção inválida, tente novamente.")
        verificar_dados(cliente)


# Cadastro do cliente
cliente = {
    "nome": input("Digite seu nome completo: "),
    "idade": int(input("Digite sua idade: ")),
    "endereco": input("Digite seu endereço: "),
    "endereco_entrega": input("Digite o endereço de entrega: ")
}


# Verificação de idade
if cliente["idade"] < 18:
    print("Desculpe, somente maiores de 18 anos podem realizar compras na Vinheira Agnello.")
    exit()


# VerificaNDO dados do cliente
print_cliente_info(cliente)
verificar_dados(cliente)


# Catálogo de vinhos
print("Conheça nosso catálogo de vinhos:")
print("1 - Vinho tinto seco - R$ 50,00")
print("2 - Vinho tinto suave - R$ 40,00")
print("3 - Vinho branco seco - R$ 45,00")
print("4 - Vinho branco suave - R$ 35,00")
print("5 - Espumante - R$ 60,00")


# Catalogo de vinhos de vinhos
produtos = {1: {"nome": "Vinho tinto seco", "preco": 50.00}, 
            2: {"nome": "Vinho tinto suave", "preco": 40.00}, 
            3: {"nome": "Vinho branco seco", "preco": 45.00},
            4: {"nome": "Vinho branco suave", "preco": 35.00}, 
            5: {"nome": "Espumante", "preco": 60.00}}

carrinho = {}
total = 0


while True:
    opcao = int(input("Digite o número do vinho que deseja comprar (0 para finalizar): "))
    if opcao == 0:
        break
    if opcao not in produtos:
        print("Opção inválida.")
    else:
        quantidade = int(input("Digite a quantidade que deseja comprar: "))
        if quantidade < 1:
            print("Quantidade inválida.")
        else:
            produto = produtos[opcao]
            preco = produto["preco"]
            subtotal = preco * quantidade
            print(f"{quantidade} x {produto['nome']}: R$ {subtotal:.2f}")
            total += subtotal
            carrinho[produto["nome"]] = quantidade


# Verificação de valor mínimo

if total < 100.00:
    print("O valor mínimo para compra é de R$ 100,00.")
    exit()


# Cálculo do frete

if total > 200.00:
    frete = 0.00
    print("Parabéns, você ganhou frete grátis!")
else:
    frete = 10.00


# Resumo da compra

print("Resumo da compra:")
for produto, quantidade in carrinho.items():
    print(f"{quantidade} x {produto}")
print(f"Valor total: R$ {total:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"Endereço de entrega: {cliente['endereco_entrega']}")
print("Obrigado pela compra, volte sempre!")
