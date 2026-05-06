# 1) (0,5 p) Crie variáveis para armazenar seu nome, nota da prova escrita, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando.
print("Olá, tudo bem")
nome = "Guilherme_Luiz"
nota_prova = 1.4
série = 3
turma = "DSC"
print("Meu nome é", nome, ", minha nota foi", nota_prova, ", minha série é", série, ", minha turma é", turma)

# 2) (0,5 p) Crie uma lista com 3 atividades que você gosta de fazer no final de semana.
Atividades = ["Desenhar", "Jogar", "Assistir series e filmes"]
atividade = ['ir ao cinema']
# 3) (1,0 p) Crie uma condição que verifica se sua nota da prova é maior que a média 1,8.
if nota_prova > 1.8:
    print("Párabens, vc passou!")
else:
    print("Sinto muito, vc reprovou.")

# 4) (1,0 p) Crie uma função mostra no terminal a quantidade de litros de água que devem ser consumidos diariamente por uma pessoa. Depois execute a função colocando um peso como parâmetro.
# Para calcular, siga a fórmula: qtd_litros =  * peso.
def calcular_agua(peso):
    qtd_litros = 0.035 * peso
    print(f"você deve beber {qtd_litros} litros de água por dia.")

calcular_agua(70)

# 5) (1,0 p) Crie um código que verifica se "estudar" existe na lista criada da questão 2. Use o laço de repetição que preferir.
encontrou = False
for atividade in Atividades:
    if atividade.lower() == "estudar":
        encontrou = True

if encontrou:
    print("A atividade 'estudar' está na lista.")
else:
    print("A atividade 'estudar' não foi encontrada.")

# 6) (1,0 p) Crie um laço de repetição que conta de 1 a 128, mas ao invés de somar 1 no contador, multiplique-o por 2.
contador = 1
while contador <= 128:
    print(contador)
    contador *= 2
