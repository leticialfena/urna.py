candidatos =[
    {
        "numero":"10",
        "nome":"leia organa",
        "partido":"aliança rebelde",
        'slogan':"a força está com você",
        "votos":0
    },
    {
        "numero":"20",
        "nome":"luke skywalker",
        "partido":"ordem jedi",
        'slogan':"use a força para o bem",
        "votos":0
    },
    {
        "numero":"30",
        "nome":"r2d2",
        "partido":"beep boop",
        'slogan':"só os loucos sabem",
        "votos":0
    },
    {
        "numero":"40",
        "nome":"goku",
        "partido":"saia jeans",
        'slogan':"kamehameha",
        "votos":0
    }
]
votos_brancos = 0
votos_nulos = 0
def pausar():
    input("\nPressione Enter para continuar...")

def menu():
    print("\n")
    print("=== \tURNA ELETRÔNICA TOPEZEIRA ===")
    print("1. listar candidatos")
    print("2. registrar voto")
    print("3. ver resultados")
    print("0. encerrar votação")

def listar_candidatos():
    print()
    print("\n=== CANDIDATOS DISPONIVEIS===")
    for candidato in candidatos:
        numero = candidato["numero"]
        nome = candidato["nome"]
        partido = candidato["partido"]
        print(f"Numero: {candidato['numero']} | Nome: {candidato['nome']} | Partido: {candidato['partido']} | Slogan: {candidato['slogan']}")

def buscar_candidato_por_numero(lista ,numero_procurado):
    for candidato in lista:
        if candidato["numero"] == numero_procurado:
            return candidato
    return None
def registrar_voto(lista):
    global votos_brancos, votos_nulos
    print()
    print("\n=== REGISTRAR VOTO ===")
    print("Digite o número do candidato ou 0 para voto em branco:").strip()
    numero_voto = input("Número do candidato: ")

    if numero_voto == "0":
        votos_brancos += 1
        print("Voto em branco registrado com sucesso!")
        return
candidato = buscar_candidato_por_numero(candidatos, numero)


if candidato is None:
        votos_nulos += 1
        print("Voto nulo registrado com sucesso!")

print()
print("candidato encontrado:")
print(f"Nome: {candidato['nome']}")
print(f"Partido: {candidato['partido']}")

confirmacao = input("Deseja confirmar o voto? (s/n): ").strip().lower()
if confirmacao == "s":
    print("Voto registrado com sucesso!")
    candidato["votos"] += 1
else:
    print("Voto cancelado.")

def exibir_resultado(lista):
    total_votos_candidato = 0

    for candidato in lista:
        total_votos_candidato += candidato["votos"]

    total_geral = total_votos_candidato + votos_brancos + votos_nulos

    print()
    print("="*40)
    print("\tResultado Parcial")
    print("="*40)

    for candidato in lista:
        nome = candidato["nome"]
        votos = candidato["votos"]

        if votos > 1:
            print(f"{nome}: {votos} voto(s)")
        else:
            print(f"{nome}: {votos} voto")

    print("-"*40)
    print(f"Votos em branco: {votos_brancos}")
    print(f"Votos nulos: {votos_nulos}")
    print(f"Total de votos: {total_geral}")

    if total_geral == 0:
        print("Ainda não há votos registrados!")
opcao = ""
while opcao != "0":
    menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        listar_candidatos()
        pausar()
    elif opcao == "2":
        registrar_voto(candidatos)
        pausar()
    elif opcao == "3":
        exibir_resultado(candidatos)
        pausar()
    elif opcao == "0":
        print("Encerrando a votação...")
    else:
        print("Opção inválida! Tente novamente.")
