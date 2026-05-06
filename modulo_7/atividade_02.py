from faker import Faker

"""Isso vai fazer com que o faker se adapte a nomes brasileiros, entre outras coisas"""
fake = Faker(
    "pt_BR"
)  # Configurando a instância do gerador (faker) para o Brasil (pt_BR)

print("\n--- [Gerando dados de clientes] ---\n")
print("-" * 75)

for i in range(1, 6):  # isso ajuda gerar 5 clientes
    nome = fake.name()  # Gerando um nome completo aleatóriamente
    email = fake.email()  # Cria um endereço de email válido
    endereco = fake.address().replace(
        "\n", ", "
    )  # Gera um endereço aleatório completo (Rua, Bairro, Cidade, Estado)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
    # Gerando uma data de nascimento dentro de uma faixa de idade
    profissao = fake.job()  # Gerando um emprego aleatório

    print(f"\n Cliente #{i}")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Nascido(a) em: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"A profissão de {nome} é: {profissao}")


print("-" * 75)
print("\n [SUCESSO] Dados gerados com maestria!\n ")
