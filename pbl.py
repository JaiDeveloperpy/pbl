# Definicao do peso das questões difíceis, médias e fáceis
pesoD = float(input("Informe o peso das questões difíceis: "))
pesoM = float(input("Informe o peso das questões médias: "))
pesoF = float(input("Informe o peso das questões fáceis: "))

# Input para o nome das equipes
equipe1 = input("Qual o nome da primeira equipe? ")
equipe2 = input("Qual o nome da segunda equipe? ")
equipe3 = input("Qual o nome da terceira equipe? ")
equipe4 = input("Qual o nome da quarta equipe? ")
equipe5 = input("Qual o nome da quinta equipe? ")

# Input para o número de rodadas
rodadas = int(input("Quantas rodadas serão? "))

# Inicializa as variáveis para armazenar os dados de cada equipe
totalQuestoesDifE1 = totalQuestoesMedE1 = totalQuestoesFacE1 = totalTempoE1 = 0
totalQuestoesDifE2 = totalQuestoesMedE2 = totalQuestoesFacE2 = totalTempoE2 = 0
totalQuestoesDifE3 = totalQuestoesMedE3 = totalQuestoesFacE3 = totalTempoE3 = 0
totalQuestoesDifE4 = totalQuestoesMedE4 = totalQuestoesFacE4 = totalTempoE4 = 0
totalQuestoesDifE5 = totalQuestoesMedE5 = totalQuestoesFacE5 = totalTempoE5 = 0

# Processa as rodadas
# Processa as rodadas
for i in range(rodadas):
    # Laço de repetição para armazenar na variável intermediária de tempo e questões
    for equipe in range(1, 6):
        questoesDif = int(input(f"Quantas questões difíceis a equipe {equipe} acertou nesta rodada? "))
        questoesMed = int(input(f"Quantas questões médias a equipe {equipe} acertou nesta rodada? "))
        questoesFac = int(input(f"Quantas questões fáceis a equipe {equipe} acertou nesta rodada? "))
        tempo = int(input(f"Quantos minutos a equipe {equipe} levou para responder nesta rodada? "))
        # Atualiza a variável de questões e tempo de cada equipe
        if equipe == 1:
            totalQuestoesDifE1 += questoesDif
            totalQuestoesMedE1 += questoesMed
            totalQuestoesFacE1 += questoesFac
            totalTempoE1 += tempo
        elif equipe == 2:
            totalQuestoesDifE2 += questoesDif
            totalQuestoesMedE2 += questoesMed
            totalQuestoesFacE2 += questoesFac
            totalTempoE2 += tempo 
        elif equipe == 3:
            totalQuestoesDifE3 += questoesDif
            totalQuestoesMedE3 += questoesMed
            totalQuestoesFacE3 += questoesFac
            totalTempoE3 += tempo
        elif equipe == 4:
            totalQuestoesDifE4 += questoesDif
            totalQuestoesMedE4 += questoesMed
            totalQuestoesFacE4 += questoesFac
            totalTempoE4 += tempo
        elif equipe == 5:
            totalQuestoesDifE5 += questoesDif
            totalQuestoesMedE5 += questoesMed
            totalQuestoesFacE5 += questoesFac
            totalTempoE5 += tempo


# Calcula a nota de cada equipe com o peso de cada questão
totalPesoE1 = (totalQuestoesDifE1 * pesoD) + (totalQuestoesMedE1 * pesoM) + (totalQuestoesFacE1 * pesoF)
totalPesoE2 = (totalQuestoesDifE2 * pesoD) + (totalQuestoesMedE2 * pesoM) + (totalQuestoesFacE2 * pesoF)
totalPesoE3 = (totalQuestoesDifE3 * pesoD) + (totalQuestoesMedE3 * pesoM) + (totalQuestoesFacE3 * pesoF)
totalPesoE4 = (totalQuestoesDifE4 * pesoD) + (totalQuestoesMedE4 * pesoM) + (totalQuestoesFacE4 * pesoF)
totalPesoE5 = (totalQuestoesDifE5 * pesoD) + (totalQuestoesMedE5 * pesoM) + (totalQuestoesFacE5 * pesoF)

# Inicializa as variáveis para guardar a posição das equipes
primeiraNota = segundaNota = terceiraNota = quartaNota = quintaNota = 0
primeiraEquipe = segundaEquipe = terceiraEquipe = quartaEquipe = quintaEquipe = ""
primeirasQuestoesDif = segundasQuestoesDif = terceirasQuestoesDif = quartasQuestoesDif = quintasQuestoesDif = 0
primeiroTempo = segundoTempo = terceiroTempo = quartoTempo = quintoTempo = 0

# Lógica para determinar o ranking considerando desempate
# Para Equipe 1
if totalPesoE1 > primeiraNota or (totalPesoE1 == primeiraNota and (totalQuestoesDifE1 > primeirasQuestoesDif or (totalQuestoesDifE1 == primeirasQuestoesDif and totalTempoE1 < primeiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = primeiraNota
    segundaEquipe = primeiraEquipe
    segundasQuestoesDif = primeirasQuestoesDif
    segundoTempo = primeiroTempo
    
    primeiraNota = totalPesoE1
    primeiraEquipe = equipe1
    primeirasQuestoesDif = totalQuestoesDifE1
    primeiroTempo = totalTempoE1
elif totalPesoE1 > segundaNota or (totalPesoE1 == segundaNota and (totalQuestoesDifE1 > segundasQuestoesDif or (totalQuestoesDifE1 == segundasQuestoesDif and totalTempoE1 < segundoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = totalPesoE1
    segundaEquipe = equipe1
    segundasQuestoesDif = totalQuestoesDifE1
    segundoTempo = totalTempoE1
elif totalPesoE1 > terceiraNota or (totalPesoE1 == terceiraNota and (totalQuestoesDifE1 > terceirasQuestoesDif or (totalQuestoesDifE1 == terceirasQuestoesDif and totalTempoE1 < terceiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = totalPesoE1
    terceiraEquipe = equipe1
    terceirasQuestoesDif = totalQuestoesDifE1
    terceiroTempo = totalTempoE1
elif totalPesoE1 > quartaNota or (totalPesoE1 == quartaNota and (totalQuestoesDifE1 > quartasQuestoesDif or (totalQuestoesDifE1 == quartasQuestoesDif and totalTempoE1 < quartoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = totalPesoE1
    quartaEquipe = equipe1
    quartasQuestoesDif = totalQuestoesDifE1
    quartoTempo = totalTempoE1
elif totalPesoE1 > quintaNota or (totalPesoE1 == quintaNota and (totalQuestoesDifE1 > quintasQuestoesDif or (totalQuestoesDifE1 == quintasQuestoesDif and totalTempoE1 < quintoTempo))):
    quintaNota = totalPesoE1
    quintaEquipe = equipe1
    quintasQuestoesDif = totalQuestoesDifE1
    quintoTempo = totalTempoE1

# Para Equipe 2
if totalPesoE2 > primeiraNota or (totalPesoE2 == primeiraNota and (totalQuestoesDifE2 > primeirasQuestoesDif or (totalQuestoesDifE2 == primeirasQuestoesDif and totalTempoE2 < primeiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = primeiraNota
    segundaEquipe = primeiraEquipe
    segundasQuestoesDif = primeirasQuestoesDif
    segundoTempo = primeiroTempo
    
    primeiraNota = totalPesoE2
    primeiraEquipe = equipe2
    primeirasQuestoesDif = totalQuestoesDifE2
    primeiroTempo = totalTempoE2
elif totalPesoE2 > segundaNota or (totalPesoE2 == segundaNota and (totalQuestoesDifE2 > segundasQuestoesDif or (totalQuestoesDifE2 == segundasQuestoesDif and totalTempoE2 < segundoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = totalPesoE2
    segundaEquipe = equipe2
    segundasQuestoesDif = totalQuestoesDifE2
    segundoTempo = totalTempoE2
elif totalPesoE2 > terceiraNota or (totalPesoE2 == terceiraNota and (totalQuestoesDifE2 > terceirasQuestoesDif or (totalQuestoesDifE2 == terceirasQuestoesDif and totalTempoE2 < terceiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = totalPesoE2
    terceiraEquipe = equipe2
    terceirasQuestoesDif = totalQuestoesDifE2
    terceiroTempo = totalTempoE2
elif totalPesoE2 > quartaNota or (totalPesoE2 == quartaNota and (totalQuestoesDifE2 > quartasQuestoesDif or (totalQuestoesDifE2 == quartasQuestoesDif and totalTempoE2 < quartoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = totalPesoE2
    quartaEquipe = equipe2
    quartasQuestoesDif = totalQuestoesDifE2
    quartoTempo = totalTempoE2
elif totalPesoE2 > quintaNota or (totalPesoE2 == quintaNota and (totalQuestoesDifE2 > quintasQuestoesDif or (totalQuestoesDifE2 == quintasQuestoesDif and totalTempoE2 < quintoTempo))):
    quintaNota = totalPesoE2
    quintaEquipe = equipe2
    quintasQuestoesDif = totalQuestoesDifE2
    quintoTempo = totalTempoE2

# Para Equipe 3
if totalPesoE3 > primeiraNota or (totalPesoE3 == primeiraNota and (totalQuestoesDifE3 > primeirasQuestoesDif or (totalQuestoesDifE3 == primeirasQuestoesDif and totalTempoE3 < primeiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = primeiraNota
    segundaEquipe = primeiraEquipe
    segundasQuestoesDif = primeirasQuestoesDif
    segundoTempo = primeiroTempo
    
    primeiraNota = totalPesoE3
    primeiraEquipe = equipe3
    primeirasQuestoesDif = totalQuestoesDifE3
    primeiroTempo = totalTempoE3
elif totalPesoE3 > segundaNota or (totalPesoE3 == segundaNota and (totalQuestoesDifE3 > segundasQuestoesDif or (totalQuestoesDifE3 == segundasQuestoesDif and totalTempoE3 < segundoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = totalPesoE3
    segundaEquipe = equipe3
    segundasQuestoesDif = totalQuestoesDifE3
    segundoTempo = totalTempoE3
elif totalPesoE3 > terceiraNota or (totalPesoE3 == terceiraNota and (totalQuestoesDifE3 > terceirasQuestoesDif or (totalQuestoesDifE3 == terceirasQuestoesDif and totalTempoE3 < terceiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = totalPesoE3
    terceiraEquipe = equipe3
    terceirasQuestoesDif = totalQuestoesDifE3
    terceiroTempo = totalTempoE3
elif totalPesoE3 > quartaNota or (totalPesoE3 == quartaNota and (totalQuestoesDifE3 > quartasQuestoesDif or (totalQuestoesDifE3 == quartasQuestoesDif and totalTempoE3 < quartoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = totalPesoE3
    quartaEquipe = equipe3
    quartasQuestoesDif = totalQuestoesDifE3
    quartoTempo = totalTempoE3
elif totalPesoE3 > quintaNota or (totalPesoE3 == quintaNota and (totalQuestoesDifE3 > quintasQuestoesDif or (totalQuestoesDifE3 == quintasQuestoesDif and totalTempoE3 < quintoTempo))):
    quintaNota = totalPesoE3
    quintaEquipe = equipe3
    quintasQuestoesDif = totalQuestoesDifE3
    quintoTempo = totalTempoE3

# Para Equipe 4
if totalPesoE4 > primeiraNota or (totalPesoE4 == primeiraNota and (totalQuestoesDifE4 > primeirasQuestoesDif or (totalQuestoesDifE4 == primeirasQuestoesDif and totalTempoE4 < primeiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = primeiraNota
    segundaEquipe = primeiraEquipe
    segundasQuestoesDif = primeirasQuestoesDif
    segundoTempo = primeiroTempo
    
    primeiraNota = totalPesoE4
    primeiraEquipe = equipe4
    primeirasQuestoesDif = totalQuestoesDifE4
    primeiroTempo = totalTempoE4
elif totalPesoE4 > segundaNota or (totalPesoE4 == segundaNota and (totalQuestoesDifE4 > segundasQuestoesDif or (totalQuestoesDifE4 == segundasQuestoesDif and totalTempoE4 < segundoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = totalPesoE4
    segundaEquipe = equipe4
    segundasQuestoesDif = totalQuestoesDifE4
    segundoTempo = totalTempoE4
elif totalPesoE4 > terceiraNota or (totalPesoE4 == terceiraNota and (totalQuestoesDifE4 > terceirasQuestoesDif or (totalQuestoesDifE4 == terceirasQuestoesDif and totalTempoE4 < terceiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = totalPesoE4
    terceiraEquipe = equipe4
    terceirasQuestoesDif = totalQuestoesDifE4
    terceiroTempo = totalTempoE4
elif totalPesoE4 > quartaNota or (totalPesoE4 == quartaNota and (totalQuestoesDifE4 > quartasQuestoesDif or (totalQuestoesDifE4 == quartasQuestoesDif and totalTempoE4 < quartoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = totalPesoE4
    quartaEquipe = equipe4
    quartasQuestoesDif = totalQuestoesDifE4
    quartoTempo = totalTempoE4
elif totalPesoE4 > quintaNota or (totalPesoE4 == quintaNota and (totalQuestoesDifE4 > quintasQuestoesDif or (totalQuestoesDifE4 == quintasQuestoesDif and totalTempoE4 < quintoTempo))):
    quintaNota = totalPesoE4
    quintaEquipe = equipe4
    quintasQuestoesDif = totalQuestoesDifE4
    quintoTempo = totalTempoE4

# Para Equipe 5
if totalPesoE5 > primeiraNota or (totalPesoE5 == primeiraNota and (totalQuestoesDifE5 > primeirasQuestoesDif or (totalQuestoesDifE5 == primeirasQuestoesDif and totalTempoE5 < primeiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = primeiraNota
    segundaEquipe = primeiraEquipe
    segundasQuestoesDif = primeirasQuestoesDif
    segundoTempo = primeiroTempo
    
    primeiraNota = totalPesoE5
    primeiraEquipe = equipe5
    primeirasQuestoesDif = totalQuestoesDifE5
    primeiroTempo = totalTempoE5
elif totalPesoE5 > segundaNota or (totalPesoE5 == segundaNota and (totalQuestoesDifE5 > segundasQuestoesDif or (totalQuestoesDifE5 == segundasQuestoesDif and totalTempoE5 < segundoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = segundaNota
    terceiraEquipe = segundaEquipe
    terceirasQuestoesDif = segundasQuestoesDif
    terceiroTempo = segundoTempo
    
    segundaNota = totalPesoE5
    segundaEquipe = equipe5
    segundasQuestoesDif = totalQuestoesDifE5
    segundoTempo = totalTempoE5
elif totalPesoE5 > terceiraNota or (totalPesoE5 == terceiraNota and (totalQuestoesDifE5 > terceirasQuestoesDif or (totalQuestoesDifE5 == terceirasQuestoesDif and totalTempoE5 < terceiroTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = terceiraNota
    quartaEquipe = terceiraEquipe
    quartasQuestoesDif = terceirasQuestoesDif
    quartoTempo = terceiroTempo
    
    terceiraNota = totalPesoE5
    terceiraEquipe = equipe5
    terceirasQuestoesDif = totalQuestoesDifE5
    terceiroTempo = totalTempoE5
elif totalPesoE5 > quartaNota or (totalPesoE5 == quartaNota and (totalQuestoesDifE5 > quartasQuestoesDif or (totalQuestoesDifE5 == quartasQuestoesDif and totalTempoE5 < quartoTempo))):
    quintaNota = quartaNota
    quintaEquipe = quartaEquipe
    quintasQuestoesDif = quartasQuestoesDif
    quintoTempo = quartoTempo
    
    quartaNota = totalPesoE5
    quartaEquipe = equipe5
    quartasQuestoesDif = totalQuestoesDifE5
    quartoTempo = totalTempoE5
elif totalPesoE5 > quintaNota or (totalPesoE5 == quintaNota and (totalQuestoesDifE5 > quintasQuestoesDif or (totalQuestoesDifE5 == quintasQuestoesDif and totalTempoE5 < quintoTempo))):
    quintaNota = totalPesoE5
    quintaEquipe = equipe5
    quintasQuestoesDif = totalQuestoesDifE5
    quintoTempo = totalTempoE5

# Saída do Ranking
print("Ranking das equipes:")
print("1ª: Equipe", primeiraEquipe, "- Nota:", primeiraNota, "- Questões Difíceis:", primeirasQuestoesDif, "- Tempo Total:", primeiroTempo)
print("2ª: Equipe", segundaEquipe, "- Nota:", segundaNota, "- Questões Difíceis:", segundasQuestoesDif, "- Tempo Total:", segundoTempo)
print("3ª: Equipe", terceiraEquipe, "- Nota:", terceiraNota, "- Questões Difíceis:", terceirasQuestoesDif, "- Tempo Total:", terceiroTempo)
print("4ª: Equipe", quartaEquipe, "- Nota:", quartaNota, "- Questões Difíceis:", quartasQuestoesDif, "- Tempo Total:", quartoTempo)
print("5ª: Equipe", quintaEquipe, "- Nota:", quintaNota, "- Questões Difíceis:", quintasQuestoesDif, "- Tempo Total:", quintoTempo)
